from flask import jsonify

from exceptions.resource_not_found import ResourceNotFound
from services.product_service_Impl import ProductServiceImpl


def route(app):
    @app.route("/products", methods=['GET'])
    def get_products():
        try:
            products = ProductServiceImpl.get_products()
            return jsonify(products), 200  # ok
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/products/<product_id>", methods=['GET'])
    def get_product_id(product_id):
        try:
            product = ProductService.get_products(int(product_id))
            return jsonify(product.json()), 200  # ok
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404
