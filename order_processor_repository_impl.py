import pyodbc
from order_processor_repository import OrderProcessorRepository

class OrderProcessorRepositoryImpl(OrderProcessorRepository):
    def __init__(self, db_connection):
        self.connection = db_connection

    def create_product(self, product):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO products (name, price, description, stockQuantity) VALUES (?, ?, ?, ?)",
                           (product.productid,product.name, product.price, product.description, product.stock_quantity))
            self.connection.commit()

    def create_customer(self, customer):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO customers (customer_id,name, email, password) VALUES (?,?, ?, ?)",
                           (customer.customer_id,customer.name, customer.email, customer.password))
            self.connection.commit()

    def delete_product(self, product_id):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
            self.connection.commit()

    def delete_customer(self, customer_id):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
            self.connection.commit()

    def add_to_cart(self, cart_id,customer, product, quantity):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO cart (cart_id,customer_id, product_id, quantity) VALUES (?,?, ?, ?)",
                           (cart_id,customer.customer_id, product.product_id, quantity))
            self.connection.commit()

    def remove_from_cart(self, customer, product):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM cart WHERE customer_id = ? AND product_id = ?",
                           (customer.customer_id, product.product_id))
            self.connection.commit()

    def get_all_from_cart(self, customer):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT p.* FROM products p JOIN cart c ON p.product_id = c.product_id WHERE c.customer_id = ?",
                           (customer.customer_id,))
            return cursor.fetchall()  # Returns a list of products

    def place_order(self, customer, products, shipping_address):
        total_price = sum(product.price for product in products)
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO orders (customer_id, total_price, shipping_address) VALUES (?, ?, ?)",
                           (customer.customer_id, total_price, shipping_address))
            order_id = cursor.lastrowid  # Get the order_id of the newly created order

            for product in products:
                cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
                               (order_id, product.product_id, 1))  # Assuming quantity is always 1 for simplicity

            self.connection.commit()

    def get_orders_by_customer(self, customer_id):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM orders WHERE customer_id = ?", (customer_id,))
            return cursor.fetchall()  # Returns a list of orders
