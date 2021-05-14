from daos.product_dao import ProductDAO
from util_project2.database_connection import connection
from models.products import Products


class ProductDAOImpl(ProductDAO):
    @classmethod
    def get_products(cls):
        try:
            sql = "SELECT * FROM products;"
            cursor = connection.cursor()
            cursor.execute(sql)
            records = cursor.fetchall()
            products = []
            for product in records:
                products.append(Products(product[0], product[1], product[2], product[3]))
            return products
        except Exception as e:
            raise ResourceNotFound(f"Credentials do not match any existing records. Please try again.")

    # @classmethod
    # def get_user_by_id(cls, user_credentials):
    #     try:
    #         sql = "SELECT * FROM users WHERE user_id= %s ;"
    #         cursor = connection.cursor()
    #         cursor.execute(sql, [user_credentials.user_id])
    #         record = cursor.fetchone()
    #         return record
    #     except Exception as e:
    #         return None
