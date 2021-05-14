from daos.orders_dao_impl import OrdersDAOImpl
from models.orders import Orders
from services.orders_service import OrdersService


class OrrdersServiceImpl(OrdersService):
    @classmethod
    def get_orders(ccls):
        try:
            list_of_orders = OrdersDAOImpl.get_orders()
            if list_of_orders:
                return [order.json() for order in list_of_orders]
            else:
                return None
        except Exception as e:
            return None
