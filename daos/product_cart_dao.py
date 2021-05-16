from models.products import Products
from util_project2.database_connection import connection


class ProductCartDAO:

    @staticmethod
    def add_product(product):
        sql = "INSERT INTO product_cart VALUES(%s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (product["productId"], product["productName"], product["productPrice"]))
        connection.commit()
        record = cursor.fetchone()
        returned_product = Products(record[0], record[1], record[2]).json()
        return returned_product
