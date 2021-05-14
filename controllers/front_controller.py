from flask import jsonify, request, make_response, render_template
from models.user_credentials import UserCredentials
from services.user_service_impl import UserServiceImpl


def route(app):
    @app.route("/", methods=['GET'])
    def login_page():
        print('here')
        response = make_response("<h1>cookie is set</h1>")
        response.set_cookie('hey', 'loooool')
        return response

    @app.route("/login", methods=['POST'])
    def users_login():
        try:
            user_credentials = UserCredentials.json_parse(request.json)
            validate_credentials = UserServiceImpl.get_user_credentials(user_credentials) #returns none if nothing found
            if validate_credentials:
                user = UserServiceImpl.get_user_by_id(validate_credentials)
                response = jsonify(user.json())
                response.set_cookie('hi', 'cookie')
                # print("hello")
                # response2 = make_response("<h1>cookie is set</h1>")
                # response2.set_cookie('hey', 'loooool')
                return response, 200
            else:
                return 'Invalid username or password', 404
        except Exception as e:
            return 'Invalid username or password', 404

    @app.route("/menu", methods=['Get'])
    def get_products():
        try:
            pass
        except Exception as e:
            return 'Need to sign in first', 404
