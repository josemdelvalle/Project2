from flask import jsonify, request
from models.user_credentials import UserCredentials
from services.user_service import UserService


def route(app):
    @app.route("/login", methods=["POST"])
    def users_login():
        print("Here")
        user_credentials = UserCredentials.json_parse(request.json)
        response = UserService.login(user_credentials)
        return jsonify(response), 200
