class Products:
    def __init__(self, product_name="", product_price=0, description=""):
        self.product_name = product_name
        self.product_price = product_price
        self.description = description

    def json(self):
        return {
            'product_name': self.product_name,
            'product_price': self.product_price,
            'description': self.description
        }

    @staticmethod
    def json_parse(json):
        products = Products()
        products.product_name = json['product_name']if "product_name" in json else None
        products.product_price = json['product_price']if "product_price" in json else None
        products.description = json['description']if "description" in json else None
        return products
