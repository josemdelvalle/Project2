from daos.product_dao import ProductDAO
from exceptions.resource_not_found import ResourceNotFound
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

    @classmethod
    def get_product_id(cls, product_id):
        sql = "SELECT * FROM products WHERE product_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [product_id])
        record = cursor.fetchone()
        if record:
            return Products(record[0], record[1], record[2], record[3])
        else:
            raise ResourceNotFound(f"Product with {product_id} - Not Found")

