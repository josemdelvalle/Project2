class ProductServiceImpl(ProductService):
    @classmethod
    def get_products(cls, products):
        response = ProductDAOImpl.get_products(products)
        if response:
            return Products(response[1], response[2], response[3]).json()
        else:
            return None