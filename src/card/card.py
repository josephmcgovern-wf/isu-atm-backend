from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel


class Card(polymodel.PolyModel):
    account = ndb.KeyProperty(kind='Account', required=True)
    bank = ndb.ComputedProperty(
        lambda self: self.account.get().bank
    )
    number = ndb.IntegerProperty(required=True)
    security_code = ndb.IntegerProperty(required=True)
    expiration_date = ndb.DateProperty(required=True)
