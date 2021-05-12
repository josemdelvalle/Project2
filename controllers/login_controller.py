def route(app):
    @app.route("/login/<username>/<password>", methods=["GET"])
    def users_login(username, password):
        user_login = UserService.login(username, password)
        if user_login:
            return jsonify(user_login.json()), 200