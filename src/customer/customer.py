from google.appengine.ext import ndb


class Customer(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    bank = ndb.KeyProperty(kind='Bank')

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def serialize_accounts(self):
        accounts = self.get_accounts()
        return [
            account.serialize() for account in accounts
        ]

    def get_accounts(self):
        from src.account.account import Account
        return Account.query(Account.owner == self.key).fetch()
