from abc import abstractmethod, ABC


class ProductDAO(ABC):
    @abstractmethod
    def get_all_products(self):
        pass
