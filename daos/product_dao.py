from abc import abstractmethod, ABC


class ProductDAO(ABC):
    @abstractmethod
    def get_products(self):
        pass
