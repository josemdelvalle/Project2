class Orders:
    def __init__(self, order_id=None, order_number=None, quantity=None, product_id=None):
        self.order_id = order_id
        self.order_number = order_number
        self.quantity = quantity
        self.product_id = product_id

    def json(self):
        return {
            'order_number': self.order_number,
            'quantity':   self.quantity,
            'product_id': self.product_id
        }

    @staticmethod
    def json_parse(json):
        orders = Orders()
        orders.product_name = json['order_number'] if "order_number" in json else None
        orders.product_price = json['quantity'] if "quantity" in json else None
        orders.description = json['product_id'] if "product_id" in json else None
        return orders
