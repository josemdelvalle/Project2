from abc import abstractmethod, ABC


class OrdersDAO(ABC):
    @abstractmethod
    def get_orders(self):
        pass
