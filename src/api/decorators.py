from flask import request

from src.atm_session.atm_session import ATMSession


ATM_SESSION_HEADER = 'X-Api-ATM-Key'


def session_required(f):
    def wrapped_function(*args, **kwargs):
        if ATM_SESSION_HEADER not in request.headers:
            return 'Unauthorized', 401
        session_key = request.headers[ATM_SESSION_HEADER]
        if not ATMSession.is_valid_session_id(session_key):
            return 'Unauthorized', 401
        return f(*args, **kwargs)
    return wrapped_function
