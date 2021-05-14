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
