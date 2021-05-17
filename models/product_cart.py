class ProductCart:

    def __init__(self, user_id=None, product_id=None, product_name=None, product_price=None, quantity=None):
        self.user_id = user_id
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.quantity = quantity

    def json(self):
        return {"userId": self.user_id,
                "productId": self.product_id,
                "productName": self.product_name,
                "productPrice": self.product_price,
                "quantity": self.quantity}

    @staticmethod
    def json_parse(json):
        product_cart = ProductCart()
        product_cart.user_id = json["userId"]
        product_cart.product_id = json["productId"]
        product_cart.product_name = json["productName"]
        product_cart.product_price = json["productPrice"]
        product_cart.quantity = json["quantity"] if "quantity" in json else 1
