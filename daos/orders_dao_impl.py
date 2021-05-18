import re

from daos.orders_dao import OrdersDAO
from models.orders import Orders
from util_project2.database_connection import connection


class OrdersDAOImpl(OrdersDAO):
    @classmethod
    def get_orders(cls):
        try:
            sql = "SELECT * FROM orders;"
            cursor = connection.cursor()
            cursor.execute(sql)
            records = cursor.fetchall()
            orders = []
            for order in records:
                orders.append(Orders(order[0], order[1], order[2], order[3]))
            return orders
        except Exception as e:
            return None

    @classmethod
    def add_order(cls, order):
        sql = "INSERT INTO orders values(default, %s, %s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (order.order_number, order.quantity, order.product_id, order.user_id))
        connection.commit()
        record = cursor.fetchone()
        returned_order = Orders(record[0], record[1], record[2], record[3], record[4])
        return returned_order

    @classmethod
    def return_largest_order_number(cls):
        sql = "SELECT MAX(order_number) FROM orders"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        record = cursor.fetchone()
        number = re.sub("[^0-9]", "", str(record))
        return int(number) + 1
