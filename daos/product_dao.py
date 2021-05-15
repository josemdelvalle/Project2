from abc import abstractmethod, ABC


class ProductDAO(ABC):
    @abstractmethod
    def get_products(self):
        pass

    @abstractmethod
    def get_product_id(self, product_id):
        pass