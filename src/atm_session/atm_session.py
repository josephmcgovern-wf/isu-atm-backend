import uuid

from google.appengine.ext import db, ndb

from src.exceptions import DuplicateSessionError


class ATMSession(ndb.Model):
    session_id = ndb.StringProperty(indexed=True)
    time_started = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def start_new(cls, customer):
        try:
            session = cls._start_new_transactionally(customer)
            return session
        except db.TransactionFailedError:
            raise DuplicateSessionError()

    @classmethod
    @ndb.transactional(retries=0)
    def _start_new_transactionally(cls, customer):
        key = ndb.Key(cls, customer.key.id())
        existing_session = key.get()
        if existing_session:
            raise DuplicateSessionError()
        else:
            session = ATMSession(
                id=customer.key.id(),
                session_id=uuid.uuid4().hex)
            session.put()
            return session

    @classmethod
    def end(cls, session_id):
        session = ATMSession.query(ATMSession.session_id == session_id).get()
        if session:
            try:
                session.end_transactionally()
            except db.TransactionFailedError:
                raise DuplicateSessionError()

    @ndb.transactional(retries=0)
    def end_transactionally(self):
        self.key.delete()

    @staticmethod
    def is_valid_session_id(session_id):
        return ATMSession.query(
            ATMSession.session_id == session_id).count() > 0
