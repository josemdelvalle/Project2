from abc import abstractmethod


class OrdersService:

    @abstractmethod
    def get_orders(self):
        pass
