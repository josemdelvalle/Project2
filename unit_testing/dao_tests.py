import unittest

from daos.product_dao_impl import ProductDAOImpl
from daos.user_dao_impl import UserDAOImpl
from models.products import Products
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
