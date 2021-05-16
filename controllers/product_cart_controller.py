from flask import json, jsonify

from services.product_cart_service import ProductCartService


def route(app):

    @app.route("/cart", methods=["POST"])
    def add_product_to_cart():
        product = json.request()
        return jsonify(ProductCartService.add_product_to_cart(product))

    @app.route("/cart", methods=["GET"])
    def get_all_products_in_cart():
        return jsonify(ProductCartService.get_all_products_from_cart())

    @app.route("/cart/<product_id>", methods=["DELETE"])
    def delete_item_from_cart(product_id):
        return jsonify(ProductCartService.delete_product_from_cart(product_id))
