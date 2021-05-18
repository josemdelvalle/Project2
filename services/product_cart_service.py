from daos.product_cart_dao import ProductCartDAO


class ProductCartService:

    product_cart_dao = ProductCartDAO

    @classmethod
    def add_product_to_cart(cls, product):
        return cls.product_cart_dao.add_product(product)

    @classmethod
    def delete_product_from_cart(cls, product_id):
        return cls.product_cart_dao.delete_product_from_cart(product_id)

    @classmethod
    def get_all_products_from_cart(cls):
        return cls.product_cart_dao.get_all_products()

    @classmethod
    def purchase_cart_items(cls, user_id):
        return cls.product_cart_dao.purchase_cart_items(user_id)
