def route(app):
    @app.route("/products", methods=['GET'])
    def get_products():
        try:
            product = ProductService.get_products()
            return jsonify(product.json()), 200  # ok
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404
