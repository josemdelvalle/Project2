from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models.order import Order
from services.orders_service_impl import OrdersServiceImpl


def route(app):
    @app.route("/orders", methods=['GET'])
    def get_orders():
        try:
            orders = OrdersServiceImpl.get_orders()
            return jsonify(orders), 200  # ok
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/order", methods=['POST'])
    def add_order():
        try:
            user_id = request.json["userId"]
            response = OrdersServiceImpl.add_order(user_id)
            print("here4")
            return jsonify(response)
        except ResourceNotFound as r:
            return r.message, 404
