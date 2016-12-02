import json

from flask import request
from flask.views import MethodView

from src.account.account import Account
from src.api.decorators import session_required
from src.customer.customer import Customer
from src.exceptions import DuplicateSessionError


class Accounts(MethodView):

    decorators = [session_required]

    def get(self, customer_id):
        customer = Customer.get_by_id(customer_id)
        if not customer:
            return 'Not found', 404
        return json.dumps(customer.serialize_accounts()), 200


class AccountsPUT(MethodView):
    decorators = [session_required]

    def __init__(self):
        self.data = request.get_json()
        self.account = 0
        self.resp = {
            'messages': [],
            'account': {}
        }

    def put(self, account_id):
        self.account = Account.get_by_id(account_id)
        if not self.account:
            return 'Not found', 404
        if not self.request_is_valid():
            return 'Invalid request', 400

        return self._put()

    def request_is_valid(self):
        raise NotImplementedError

    def _put(self):
        raise NotImplementedError

    def make_response(self, message):
        resp_data = {
            'message': message,
            'account': self.account.serialize()
        }
        return json.dumps(resp_data), 200


class TransferFunds(AccountsPUT):

    def _put(self):
        self.target_account = Account.get_by_id(self.data['target_account_id'])
        if not self.target_account:
            return 'Target account not found', 404
        try:
            self.account.transfer(self.data['amount'], self.target_account)
        except DuplicateSessionError:
            return 'This transaction is already under way', 400
        except AssertionError as e:
            return e.message, 400
        return self.make_response('Transfer successful')

    def request_is_valid(self):
        return all([
            isinstance(int, self.data.get('target_account_id')),
            type(self.data.get('amount')) in [float, int]
        ])

    def make_response(self, message):
        resp_data = {
            'message': message,
            'account': self.account.serialize(),
            'target_account': self.target_account.serialize()
        }
        return json.dumps(resp_data), 200


class Withdraw(AccountsPUT):

    def _put(self):
        try:
            self.account.withdraw(self.data['amount'])
        except DuplicateSessionError:
            return 'This transaction is already under way', 400
        except AssertionError as e:
            return e.message, 400

        return self.make_response('Withdraw successful')

    def request_is_valid(self):
        return type(self.data.get('amount')) in [float, int]


class Deposit(AccountsPUT):

    def _put(self):
        try:
            self.account.deposit(self.data['amount'])
        except DuplicateSessionError:
            return 'This transaction is already under way', 400
        return self.make_response('Deposit successful')

    def request_is_valid(self):
        return type(self.data.get('amount')) in [float, int]


def setup_urls(app):
    app.add_url_rule(
        '/api/account/<int:customer_id>/',
        view_func=Accounts.as_view('accounts')
    )
    app.add_url_rule(
        '/api/account/<int:account_id>/withdraw/',
        view_func=Withdraw.as_view('withdraw')
    )
    app.add_url_rule(
        '/api/account/<int:account_id>/transfer/',
        view_func=TransferFunds.as_view('transfer')
    )
    app.add_url_rule(
        '/api/account/<int:account_id>/deposit/',
        view_func=Deposit.as_view('deposit')
    )
