from flask import jsonify, request
from models.user_credentials import UserCredentials
from services.user_service_impl import UserServiceImpl


def route(app):
    @app.route("/login", methods=['POST'])
    def users_login():
        user_credentials = UserCredentials.json_parse(request.json)
        print(user_credentials.user_name, user_credentials.password)
        response = UserServiceImpl.get_user_credentials(user_credentials)
        if response:
            return jsonify(response), 200
        else:
            return 'Invalid username or password', 404
