from abc import abstractmethod


class ProductService:

    @abstractmethod
    def get_products(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass