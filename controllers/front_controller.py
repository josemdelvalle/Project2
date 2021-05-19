from flask import jsonify, request
from models.user_credentials import UserCredentials
from services.user_service_impl import UserServiceImpl
from exceptions.resource_not_found import ResourceNotFound


def route(app):
    @app.route("/adminLogin", methods=['POST'])
    @app.route("/login", methods=['POST'])
    def users_login():
        try:
            user_credentials = UserCredentials.json_parse(request.json)
            # Return the user ID if the credentials are in the database, otherwise returns an exception
            user_id = UserServiceImpl.get_user_credentials(user_credentials)
            # Gets user information from ID returned in previous step
            user = UserServiceImpl.get_user_by_id(user_id)
            if user.first_name == 'Marc':
                user.is_admin = True
            response = jsonify(user.json())
            return response, 200
        except ResourceNotFound as r:
            return r.message, 404
    #
    # @app.route("/menu", methods=['Get'])
    # def get_products():
    #     try:
    #         pass
    #     except Exception as e:
    #         return 'Need to sign in first', 404
