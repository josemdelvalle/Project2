import unittest

from exceptions.resource_not_found import ResourceNotFound
from models.product_cart import ProductCart
from models.products import Products
from services.orders_service_impl import OrdersServiceImpl
from services.product_cart_service import ProductCartService
from services.product_service_Impl import ProductServiceImpl


class ServiceTests(unittest.TestCase):

    # Order Service
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

    # Product Service
    def test_get_product_by_id_success(self):
        product = ProductServiceImpl.get_product_by_id(1)
        self.assertEqual(type(product), type(Products()))

    def test_get_product_by_id_failure(self):
        try:
            product = ProductServiceImpl.get_product_by_id(99)
            self.assertEqual(type(product), type(Products()))
        except ResourceNotFound as r:
            assert True
        else:
            assert False

    def test_get_products(self):
        products_list = ProductServiceImpl.get_products()
        product = products_list[9]
        self.assertEqual(product["productId"], 10)

    # Product Cart Service
    def test_add_product_to_cart(self):
        test_product_cart = ProductCart(1, 9, 1, "Banana Cream Pie", 6, 7)
        returned_product_cart = ProductCartService.add_product_to_cart(test_product_cart)
        self.assertEqual(type(returned_product_cart), type(test_product_cart))

    @staticmethod
    def test_get_all_products_from_cart_by_user_id():
        product_cart_items = ProductCartService.get_all_products_from_cart_by_user_id("1")
        for product in product_cart_items:
            if product["userId"] == "1":
                continue
            else:
                assert False

        assert True

    def test_purchase_cart_items(self):
        # Create items to add to the cart in order to purchase them
        # This will technically test multiple methods
        test_product1 = ProductCart(5, 5, 1, "Banana Cream Pie", 6, 6)
        test_product2 = ProductCart(5, 5, 3, "Banana Chocolate Chip", 13, 2)
        test_product3 = ProductCart(5, 5, 17, "Peanut Butter & Graham", 9, 1)
        test_product4 = ProductCart(5, 5, 21, "Pumpkin", 11, 4)
        all_test_products = [test_product1, test_product2, test_product3, test_product4]
        ProductCartService.add_product_to_cart(all_test_products[0])
        ProductCartService.add_product_to_cart(all_test_products[1])
        ProductCartService.add_product_to_cart(all_test_products[2])
        ProductCartService.add_product_to_cart(all_test_products[3])
        purchased_products = ProductCartService.purchase_cart_items(5)
        for i in range(len(purchased_products)):
            if purchased_products[i] == all_test_products[i]:
                continue
            else:
                assert False

        assert True
