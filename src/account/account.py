from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel


class Account(polymodel.PolyModel):
    bank = ndb.KeyProperty(kind='Bank', required=True)
    interest = ndb.FloatProperty(default=0)
    owner = ndb.KeyProperty(kind='Customer', required=True)
    pin = ndb.IntegerProperty(required=True)
    nickname = ndb.StringProperty()
    total_money = ndb.FloatProperty()

    @property
    def account_type(self):
        raise NotImplementedError

    def serialize(self):
        d = self._to_dict()
        d['bank'] = self.bank.get().name
        d['id'] = self.key.id()
        d['owner'] = self.owner.get().full_name
        d['account_type'] = self.account_type
        del d['pin']
        del d['class_']
        return d

    @ndb.transactional(retries=0)
    def withdraw(self, amount):
        assert self.total_money > amount, 'Insufficient funds'
        self.total_money -= amount
        self.put()

    @ndb.transactional(retries=0)
    def deposit(self, amount):
        self.total_money += amount
        self.put()

    @ndb.transactional(retries=0)
    def transfer_funds(self, amount, to_account):
        m = 'Transfers must be to the same person'
        assert to_account.owner == self.key, m
        assert self.total_money > amount, 'Insufficient funds'
        self.total_money -= amount
        to_account.total_moeny += amount
        ndb.put_multi([self, to_account])


class CheckingAccount(Account):

    @property
    def account_type(self):
        return 'checking'


class SavingsAccount(Account):

    @property
    def account_type(self):
        return 'savings'
