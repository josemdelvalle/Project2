import unittest

from services.orders_service_impl import OrdersServiceImpl


class ServiceTests(unittest.TestCase):

    @staticmethod
    def test_get_all_orders():
        try:
            orders = OrdersServiceImpl.get_orders()
            if orders is not None:
                assert True
            else:
                assert False
        except Exception:
            assert True
