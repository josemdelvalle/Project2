class ProductCart:

    def __init__(self, cart_id=None, product_id=None, user_id=None, product_name=None, product_price=None,
                 quantity=None):
        self.cart_id = cart_id
        self.user_id = user_id
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.quantity = quantity

    def json(self):
        return {"cartId": self.cart_id,
                "userId": self.user_id,
                "productId": self.product_id,
                "productName": self.product_name,
                "productPrice": float(self.product_price),
                "quantity": self.quantity}

    @staticmethod
    def json_parse(json):
        product_cart = ProductCart()
        product_cart.cart_id = json["cartId"] if "cartId" in json else None
        product_cart.user_id = json["userId"] if "userId" in json else None
        product_cart.product_id = json["productId"] if "productId" in json else None
        product_cart.product_name = json["productName"] if "productName" in json else None
        product_cart.product_price = json["productPrice"] if "productPrice" in json else None
        product_cart.quantity = json["quantity"] if "quantity" in json else None
        return product_cart
