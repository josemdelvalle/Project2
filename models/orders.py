class Orders:
    def __init__(self, order_id=None, order_number=None, quantity=None, product_id=None, user_id=None):
        self.order_id = order_id
        self.order_number = order_number
        self.quantity = quantity
        self.product_id = product_id
        self.user_id = user_id

    def json(self):
        return {
            "orderId": self.order_id,
            'orderNumber': self.order_number,
            'quantity':   self.quantity,
            'productId': self.product_id,
            "userId": self.user_id
        }

    @staticmethod
    def json_parse(json):
        orders = Orders()
        orders.product_name = json['orderNumber'] if "order_number" in json else None
        orders.product_price = json['quantity'] if "quantity" in json else None
        orders.description = json['productId'] if "product_id" in json else None
        orders.user_id = json["userId"] if "userId" in json else None
        return orders
