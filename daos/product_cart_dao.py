from daos.orders_dao_impl import OrdersDAOImpl
from exceptions.resource_not_found import ResourceNotFound
from models.orders import Orders
from models.product_cart import ProductCart
from util_project2.database_connection import connection


class ProductCartDAO:

    @staticmethod
    def add_product(product_cart):
        sql = "INSERT INTO product_cart VALUES(default,%s, %s, %s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [product_cart.product_id, product_cart.user_id,
                             product_cart.product_name, product_cart.product_price, product_cart.quantity])
        connection.commit()
        record = cursor.fetchone()
        if record:
            returned_product = ProductCart(record[0], record[1], record[2], record[3], record[4], record[5])
            return returned_product
        else:
            raise ResourceNotFound(f"User with ID {product_cart.user_id} does not exist. Please try again.")

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

    @staticmethod
    def get_all_products_from_cart_by_user_id(user_id):
        sql = "SELECT * FROM product_cart where user_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()
        records = cursor.fetchall()
        cart_list = []
        if records:
            for record in records:
                product = ProductCart(record[0], record[1], record[2], record[3], record[4], record[5])
                cart_list.append(product)
            return cart_list
        else:
            raise ResourceNotFound(f"User with ID {user_id} does not exist. Please try again.")

    @staticmethod
    def purchase_cart_items(user_id):
        # First want to grab everything from the databse to add to the orders table
        sql = "SELECT * FROM product_cart WHERE user_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()
        records = cursor.fetchall()
        # Then hold each item into a list to be exported to the orders table
        purchased_products = []
        order = Orders()
        for record in records:
            product = ProductCart(record[0], record[1], record[2], record[3], record[4])
            purchased_products.append(product.json())

        order_number = OrdersDAOImpl.return_largest_order_number()
        for product in purchased_products:
            order.order_number = order_number
            order.quantity = product.quantity
            order.product_id = product.product_id
            order.user_id = product.user_id
            OrdersDAOImpl.add_order(order)
        return purchased_products
