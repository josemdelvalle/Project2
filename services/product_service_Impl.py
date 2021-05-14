from daos.product_dao_impl import ProductDAOImpl
from models.products import Products
from services.product_service import ProductService


class ProductServiceImpl(ProductService):
    @classmethod
    def get_products(cls):
        try:
            list_of_products = ProductDAOImpl.get_products()
            if list_of_products:
                return [product.json() for product in list_of_products]
            else:
                return None
        except Exception as e:
            return None
