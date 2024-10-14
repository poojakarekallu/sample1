from abc import ABC, abstractmethod

class OrderProcessorRepository(ABC):

    @abstractmethod
    def create_product(self, product):
        """Add a new product to the database."""
        pass

    @abstractmethod
    def create_customer(self, customer):
        """Register a new customer in the database."""
        pass

    @abstractmethod
    def delete_product(self, product_id):
        """Remove a product from the database."""
        pass

    @abstractmethod
    def delete_customer(self, customer_id):
        """Remove a customer from the database."""
        pass

    @abstractmethod
    def add_to_cart(self, customer, product, quantity):
        """Add a product to the customer's cart."""
        pass

    @abstractmethod
    def remove_from_cart(self, customer, product):
        """Remove a product from the customer's cart."""
        pass

    @abstractmethod
    def get_all_from_cart(self, customer):
        """Retrieve all products in the customer's cart."""
        pass

    @abstractmethod
    def place_order(self, customer, products, shipping_address):
        """Place an order for the customer."""
        pass

    @abstractmethod
    def get_orders_by_customer(self, customer_id):
        """Retrieve all orders for a specific customer."""
        pass
