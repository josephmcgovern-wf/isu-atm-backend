from datetime import datetime
import json

from flask import request
from flask.views import MethodView

from src.account.account import Account
from src.atm_session.atm_session import ATMSession
from src.bank.bank import Bank
from src.customer.customer import Customer
from src.exceptions import DuplicateSessionError


class OpenATMSession(MethodView):

    def post(self, bank_name):
        bank = Bank.query(Bank.name == bank_name).get()
        if not bank:
            return 'Bank not found', 404

        data = request.get_json()
        if not self._is_valid_request(data):
            return 'Invalid request', 400

        card_number = data['card_number']
        security_code = data['security_code']
        expiration_date = datetime.strptime(
            data['expiration_date'], '%m/%y').date()
        pin = data['pin']

        card = bank.get_card(card_number, security_code, expiration_date)
        if not card:
            return 'Card not found', 404

        account = card.account.get()
        if account.pin != pin:
            return 'Invalid card', 400

        owner = account.owner.get()
        try:
            session = ATMSession.start_new(owner)
        except DuplicateSessionError:
            return 'This user is already using an ATM', 400

        response = {
            'token': session.session_id,
            'accounts': owner.serialize_accounts()
        }
        return json.dumps(response), 200

    def _is_valid_request(self, data):
        return all([
            'card_number' in data,
            'security_code' in data,
            'expiration_date' in data,
            'pin' in data
        ])


class EndATMSession(MethodView):

    def post(self, session_id):
        try:
            ATMSession.end(session_id)
        except DuplicateSessionError:
            return 'Could not end session', 400
        return 'Session ended', 200


def setup_urls(app):
    app.add_url_rule(
        '/api/atm/<bank_name>/start_session/',
        view_func=OpenATMSession.as_view('atm.start_session')
    )
    app.add_url_rule(
        '/api/atm/<session_id>/end/',
        view_func=EndATMSession.as_view('atm.end_session')
    )
