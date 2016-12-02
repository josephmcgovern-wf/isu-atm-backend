from google.appengine.ext import ndb


class Bank(ndb.Model):
    name = ndb.StringProperty(required=True)

    def get_card(self, card_number, security_code, expiration_date):
        from src.card.card import Card
        return Card.query(
            Card.number == card_number,
            Card.security_code == security_code,
            Card.bank == self.key,
            Card.expiration_date == expiration_date).get()
