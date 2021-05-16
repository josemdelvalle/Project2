from daos.product_dao_impl import ProductDAOImpl
from models.products import Products
from services.product_service import ProductService


class ProductServiceImpl(ProductService):
    @classmethod
    def get_product_by_id(cls, product_id):
        product=ProductDAOImpl.get_product_id(product_id)
        return product

    @classmethod
    def get_products(cls):
        list_of_products = ProductDAOImpl.get_products()
        return [product.json() for product in list_of_products]

    # class UserServiceImpl(UserService):
    #     @classmethod
    #     def get_product_id(cls, product_id):
    #         return ProductDAOImpl.get_product_id(product_id)

