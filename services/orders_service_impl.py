from daos.orders_dao_impl import OrdersDAOImpl
from services.orders_service import OrdersService


class OrdersServiceImpl(OrdersService):
    @classmethod
    def add_order(cls, user_id):
        response = OrdersDAOImpl.add_order(user_id)
        return response

    @classmethod
    def get_orders(cls):
        try:
            list_of_orders = OrdersDAOImpl.get_orders()
            if list_of_orders:
                return [order.json() for order in list_of_orders]
            else:
                return None
        except Exception as e:
            return None
