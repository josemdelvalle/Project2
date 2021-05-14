from flask import jsonify

from exceptions.resource_not_found import ResourceNotFound
from services.orders_service_impl import OrrdersServiceImpl

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
