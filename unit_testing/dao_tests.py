import unittest

from daos.orders_dao_impl import OrdersDAOImpl
from daos.product_cart_dao import ProductCartDAO
from daos.product_dao_impl import ProductDAOImpl
from daos.user_dao_impl import UserDAOImpl
from models.orders import Orders
from models.product_cart import ProductCart
from models.user import User
from models.user_credentials import UserCredentials


class DAOTests(unittest.TestCase):
    def test_get_all_products(self):
        products = ProductDAOImpl().get_products()
        test_product = {
            "productId": 9,
            "description": "Vanilla Ice Cream with Chocolate Fudge",
            "productName": "Fudge Ripple",
            "productPrice": 24.0
        }
        for product in products:
            try:
                return self.assertDictEqual(product.json(), test_product)
            except AssertionError:
                continue

        assert False

    def test_get_user_by_id(self):
        user = UserDAOImpl.get_user_by_id(1)
        expected = User(1, "Jose", "Del")
        self.assertDictEqual(user.json(), expected.json())

    def test_get_user_credentials(self):
        credentials = UserCredentials("jose", "12345", 1)
        test_credentials = UserDAOImpl.get_user_credentials(credentials)
        self.assertDictEqual(credentials.json(), test_credentials.json())

    def test_add_product_to_cart(self):
        test_product = {
            "userId": 1,
            "productId": 9,
            "productName": "Fudge Ripple",
            "productPrice": 24.0,
            "quantity": 1}

        product_cart_dao = ProductCartDAO()
        returned_product = product_cart_dao.add_product(test_product)
        self.assertEqual(returned_product["productId"], test_product["productId"])

    def test_get_all_cart_items(self):
        all_products = ProductCartDAO.get_all_products()
        self.assertIsNotNone(all_products)

    def test_delete_product_from_cart(self):
        product = ProductCartDAO.delete_product_from_cart(9)
        self.assertEqual(product["productId"], 9)

    def test_purchase_order(self):
        test_product = ProductCart(1, "9", "Fudge Ripple", 24.0, 1)
        order = Orders(1, 1, test_product.quantity, test_product.product_id, test_product.user_id)
        returned_order = OrdersDAOImpl.add_order(order)
        self.assertEqual(returned_order.order_number, order.order_number)

    def test_order_number(self):
        self.assertIsNotNone(OrdersDAOImpl.return_largest_order_number())
