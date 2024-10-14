class Product:
    def __init__(self, product_id=None, name=None, price=None, description=None, stock_quantity=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity

    # Getters and Setters
    def get_product_id(self):
        return self.product_id

    def set_product_id(self, product_id):
        self.product_id = product_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_stock_quantity(self):
        return self.stock_quantity

    def set_stock_quantity(self, stock_quantity):
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price})"
