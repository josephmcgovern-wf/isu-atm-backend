import base64

from google.appengine.ext import ndb


class User(ndb.Model):
    email = ndb.StringProperty(required=True)
    token = ndb.StringProperty(required=True)

    @staticmethod
    def add(email, password):
        token = User.compute_token(email, password)
        if User.email_already_taken(email):
            raise Exception('That email is already taken')
        if User.user_exists(token):
            raise Exception('That token already exists')
        user = User(email=email, token=token)
        user.put()
        return user

    @staticmethod
    def compute_token(email, password):
        unencoded = '{email}:{password}'.format(
            email=email, password=password
        )
        return base64.b64encode(unencoded)

    @staticmethod
    def email_already_taken(email):
        return User.query(User.email == email).count() > 0

    @staticmethod
    def user_exists(token):
        return User.query(User.token == token).count() > 0

    @staticmethod
    def get_user_from_request_auth(auth):
        if auth is None:
            return None
        token = User.compute_token(auth['username'], auth['password'])
        return User.query(User.token == token).get()

    def serialize(self):
        d = self._to_dict()
        del d['token']
        return d
