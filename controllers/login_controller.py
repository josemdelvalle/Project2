def route(app):
    @app.route("/login/<username>/<password>", methods=["GET"])
    def users_login(username, password):
        userlogin = UserService.login(username, password)
        if userlogin:
            return jsonify(logininfo.json()), 200