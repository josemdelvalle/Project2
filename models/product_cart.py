class ProductCart:

    def __init__(self, product_id=None, product_name=None, product_price=None):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    def json(self):
        return {"productId": self.product_id,
                "productName": self.product_name,
                "productPrice": self.product_price}

    @staticmethod
    def json_parse(json):
        product_cart = ProductCart()
        product_cart.product_id = json["productId"]
        product_cart.product_name = json["productName"]
        product_cart.product_price = json["productPrice"]
