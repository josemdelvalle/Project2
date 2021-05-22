import re

from daos.orders_dao import OrdersDAO
from exceptions.resource_not_found import ResourceNotFound
from models.order import Order
from util_project2.database_connection import connection


class OrdersDAOImpl(OrdersDAO):
    @classmethod
    def get_orders(cls):
        sql = "SELECT * FROM orders;"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        orders = []
        if records:
            for order in records:
                orders.append(Order(order[0], order[1], order[2], order[3]))
            return orders
        else:
            raise ResourceNotFound(f"Order does not exist. Please try again.")

    @classmethod
    def add_order(cls, order):
        try:
            list_param = []
            order_number = OrdersDAOImpl.return_largest_order_number()
            for orderx in order:
                list_param.append((order_number, orderx.quantity, orderx.product_id, orderx.user_id))
            sql = "INSERT INTO orders values(default, %s, %s, %s, %s) RETURNING *"
            cursor = connection.cursor()
            cursor.executemany(sql, list_param)
            connection.commit()
            return "Order submitted", 200
        except Exception as e:
            raise ResourceNotFound(f"Order does not exist. Please try again.")

    @classmethod
    def return_largest_order_number(cls):
        sql = "SELECT MAX(order_number) FROM orders"
        cursor = connection.cursor()
        cursor.execute(sql)
        record = cursor.fetchone()
        if not record[0]:
            record = 0
        number = re.sub("[^0-9]", "", str(record))
        return int(number) + 1
