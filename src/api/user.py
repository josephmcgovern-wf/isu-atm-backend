import json

from flask import request
from flask.views import MethodView

from src.user.user import User


class UserEndpoint(MethodView):

    def get(self):
        '''
        Basic auth endpoint
        '''
        user = User.get_user_from_request_auth(request.authorization)
        if not user:
            return 'Not found', 404

        return json.dumps(user.serialize()), 200

    def post(self):
        '''
        Endpoint to create a user
        '''
        data = request.get_json()
        if not self._post_request_is_valid(data):
            return 'Invalid request', 400

        try:
            User.add(data['email'], data['password'])
            return 'User created', 200
        except Exception as e:
            return e.message, 400

    def _post_request_is_valid(self, data):
        return all([
            'email' in data,
            'password' in data
        ])


def setup_urls(app):
    app.add_url_rule(
        '/user/', methods=['GET', 'POST'],
        view_func=UserEndpoint.as_view('api.user')
    )
