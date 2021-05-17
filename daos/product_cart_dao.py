from models.product_cart import ProductCart
from models.products import Products
from util_project2.database_connection import connection


class ProductCartDAO:

    @staticmethod
    def add_product(product):
        sql = "INSERT INTO product_cart VALUES(%s, %s, %s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (product["userId"], product["productId"], product["productName"],
                             product["productPrice"], product["quantity"]))
        connection.commit()
        record = cursor.fetchone()
        returned_product = ProductCart(record[0], record[1], record[2], record[3], record[4]).json()
        return returned_product

    @staticmethod
    def delete_product_from_cart(product_id):
        sql = "DELETE FROM product_cart WHERE product_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [product_id])
        connection.commit()
        record = cursor.fetchone()
        if record:
            return ProductCart(record[0], record[1], record[2], record[3], record[4]).json()
        else:
            return None

    @staticmethod
    def get_all_products():
        sql = "SELECT * FROM product_cart"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        records = cursor.fetchall()
        cart_list = []
        for record in records:
            product = ProductCart(record[0], record[1], record[2], record[3], record[4])
            cart_list.append(product.json())

        return cart_list
