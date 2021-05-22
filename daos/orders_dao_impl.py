import re

from daos.orders_dao import OrdersDAO
from daos.product_cart_dao import ProductCartDAO
from exceptions.resource_not_found import ResourceNotFound
from models.order import Order
from util_project2.database_connection import connection


class OrdersDAOImpl(OrdersDAO):
    @classmethod
    def get_orders(cls):
        try:
            sql = "SELECT * FROM orders"
            cursor = connection.cursor()
            cursor.execute(sql)
            records = cursor.fetchall()
            orders = []
            for order in records:
                orders.append(Order(order[0], order[1], order[2], order[3]))
            return orders
        except Exception as e:
            return None

    @classmethod
    def add_order(cls, user_id):
        try:
            order_num = cls.return_largest_order_number()
            products_in_cart = ProductCartDAO.get_all_products_from_cart_by_user_id(user_id)
            data = []
            for cart_item in products_in_cart:
                data.append((order_num, cart_item.quantity, cart_item.product_id, user_id))
            sql = "INSERT INTO orders values(default, %s, %s, %s, %s) RETURNING *"
            cursor = connection.cursor()
            cursor.executemany(sql, data)
            connection.commit()

            ProductCartDAO.delete_cart_items_from_user_id(user_id)

            return "Order submitted", 200
        except Exception as e:
            raise ResourceNotFound(f"Order does not exist. Please try again.")

    @classmethod
    def return_largest_order_number(cls):
        sql = "SELECT MAX(order_number) FROM orders"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        record = cursor.fetchone()
        if not record[0]:
            record = 1
        number = re.sub("[^0-9]", "", str(record))
        return int(number) + 1
