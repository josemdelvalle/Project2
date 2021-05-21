import unittest

from daos.orders_dao_impl import OrdersDAOImpl
from daos.product_cart_dao import ProductCartDAO
from daos.product_dao_impl import ProductDAOImpl
from daos.user_dao_impl import UserDAOImpl
from exceptions.resource_not_found import ResourceNotFound
from models.orders import Orders
from models.product_cart import ProductCart
from models.user import User
from models.user_credentials import UserCredentials


class DAOTests(unittest.TestCase):
    # Product DAO
    def test_get_all_products(self):
        products = ProductDAOImpl().get_products()
        self.assertEqual(type(products), type([]))

    def test_get_product_by_id_success(self):
        test_product = {
            "productId": 9,
            "description": "Vanilla Ice Cream with Chocolate Fudge",
            "productName": "Fudge Ripple",
            "productPrice": 24.0,
            "productType": "MilkShake"
        }
        product = ProductDAOImpl().get_product_id(test_product["productId"])
        self.assertDictEqual(product.json(), test_product)

    def test_get_product_by_id_failure(self):
        test_product = {
            "productId": -1,
            "description": "Does not exist in this store",
            "productName": "Garbage",
            "productPrice": 0.0,
            "productType": "Garbage"
        }

        try:
            ProductDAOImpl().get_product_id(test_product["productId"])
            raise AssertionError("There is no product by that ID.")
        except ResourceNotFound as r:
            self.assertEqual(r.message, "Product with ID -1 - Not Found")

    # User DAO
    def test_get_user_by_id_success(self):
        user = UserDAOImpl.get_user_by_id(1)
        expected = User(1, "Jose", "Del Valle")
        self.assertDictEqual(user.json(), expected.json())

    def test_get_user_by_id_failure(self):
        try:
            UserDAOImpl.get_user_by_id(-1)
            raise AssertionError("No User exists by that id.")
        except ResourceNotFound as r:
            self.assertEqual(r.message, "User with ID -1 does not exist. Please try again.")

    def test_get_user_credentials(self):
        credentials = UserCredentials("jose", "12345", 1)
        test_credentials = UserDAOImpl.get_user_credentials(credentials)
        self.assertDictEqual(credentials.json(), test_credentials.json())

    # Product Cart DAO
    def test_add_product_to_cart(self):
        test_product = {
            "userId": 1,
            "productId": 9,
            "productName": "Fudge Ripple",
            "productPrice": 24.0,
            "quantity": 1}

        product_cart_dao = ProductCartDAO()
        returned_product = product_cart_dao.add_product(test_product)
        self.assertEqual(returned_product.product_id, test_product["productId"])

    def test_get_all_cart_items(self):
        all_products = ProductCartDAO.get_all_products()
        self.assertIsNotNone(all_products)

    def test_delete_product_from_cart(self):
        product = ProductCartDAO.delete_product_from_cart(9)
        self.assertEqual(product["productId"], 9)

    def test_purchase_order(self):
        # test_product = ProductCart(1, 9, "Fudge Ripple", 24.0, 1)
        order = Orders(1, 1, 1, 9, 1)
        returned_order = OrdersDAOImpl.add_order(order)
        self.assertEqual(returned_order.order_number, order.order_number)

    # Order DAO
    def test_order_number(self):
        self.assertIsNotNone(OrdersDAOImpl.return_largest_order_number())
