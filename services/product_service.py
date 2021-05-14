from abc import abstractmethod


class ProductService:

    @abstractmethod
    def get_products(self):
        pass
