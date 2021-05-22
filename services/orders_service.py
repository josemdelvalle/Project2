from abc import abstractmethod


class OrdersService:

    @abstractmethod
    def get_orders(self):
        pass

    @abstractmethod
    def add_order(self, user_id):
        pass

