from daos.orders_dao import OrdersDAO
from util_project2.database_connection import connection
from models.orders import Orders

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

