from daos.product_dao import ProductDAO
from util_project2.db_connection import connection


class ProductDAOImpl(ProductDAO):
    @classmethod
    def get_all_products(cls):
        try:
            sql = "SELECT * FROM products ;"
            cursor = connection.cursor()
            cursor.execute(sql)
            records = cursor.fetchall()
            return records
        except Exception as e:
            return None
