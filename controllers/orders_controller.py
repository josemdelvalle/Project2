from flask import jsonify , request

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
            print("Here")
            order = Order.json_parse(request.json)
            response = OrdersServiceImpl.add_order(order)
            return jsonify(response.json())
        except ResourceNotFound as r:
            return r.message, 404
