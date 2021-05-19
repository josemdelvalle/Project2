from flask import json, jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models.product_cart import ProductCart
from services.product_cart_service import ProductCartService
from services.product_service_Impl import ProductServiceImpl
from services.user_service_impl import UserServiceImpl


def route(app):
    @app.route("/cart", methods=["POST"])
    def add_product_to_cart():
        try:
            product_cart = ProductCart.json_parse(request.json)
            check_user = UserServiceImpl.get_user_by_id(product_cart.user_id)
            check_product = ProductServiceImpl.get_product_by_id(product_cart.product_id)
            product_cart.product_name = check_product.product_name
            product_cart.product_price = check_product.product_price
            return jsonify(ProductCartService.add_product_to_cart(product_cart).json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/cart", methods=["GET"])
    def get_all_products_in_cart():
        return jsonify(ProductCartService.get_all_products_from_cart())

    @app.route("/cart/<product_id>", methods=["DELETE"])
    def delete_item_from_cart(product_id):
        return jsonify(ProductCartService.delete_product_from_cart(product_id))

    @app.route("/purchase/<user_id>", methods=["POST"])
    def purchase_cart_items(user_id):
        ProductCartService.purchase_cart_items(user_id)
