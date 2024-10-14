from db_connection import DBConnection
from order_processor_repository_impl import OrderProcessorRepositoryImpl
from customer import Customer
from product import Product

def main():
    # Set up the database connection
    db_connection = DBConnection()
    connection = db_connection.get_connection()

    # Create the repository instance
    order_processor = OrderProcessorRepositoryImpl(connection)

    while True:
        print("\n--- eCommerce Application ---")
        print("1. Register Customer")
        print("2. Create Product")
        print("3. Delete Product")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Place Order")
        print("7. View Customer Orders")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Register Customer
            customer_id=int(input("enter id:"))
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            customer = Customer(customer_id=customer_id,name=name, email=email, password=password)
            order_processor.create_customer(customer)
            print("Customer registered successfully.")

        elif choice == '2':
            # Create Product
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            description = input("Enter product description: ")
            stock_quantity = int(input("Enter stock quantity: "))
            product = Product(name=name, price=price, description=description, stock_quantity=stock_quantity)
            order_processor.create_product(product)
            print("Product created successfully.")

        elif choice == '3':
            # Delete Product
            product_id = int(input("Enter product ID to delete: "))
            order_processor.delete_product(product_id)
            print("Product deleted successfully.")

        elif choice == '4':
            # Add to Cart
            cart_id = int(input("Enter cart ID: "))
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            customer = Customer(customer_id=customer_id)  # Create customer instance for reference
            product = Product(product_id=product_id)      # Create product instance for reference
            order_processor.add_to_cart(cart_id ,customer, product, quantity)
            print("Product added to cart successfully.")

        elif choice == '5':
            # View Cart
            customer_id = int(input("Enter customer ID: "))
            customer = Customer(customer_id=customer_id)
            cart_items = order_processor.get_all_from_cart(customer)
            print("Items in Cart:")
            for item in cart_items:
                print(f"- {item.name}: {item.price}")

        elif choice == '6':
            # Place Order
            customer_id = int(input("Enter customer ID: "))
            shipping_address = input("Enter shipping address: ")
            # Assume we are getting product IDs from the cart for the order
            customer = Customer(customer_id=customer_id)
            # This is a placeholder for products, you would typically retrieve these from the cart
            products = []  # Populate with actual product instances
            order_processor.place_order(customer, products, shipping_address)
            print("Order placed successfully.")

        elif choice == '7':
            # View Customer Orders
            customer_id = int(input("Enter customer ID: "))
            orders = order_processor.get_orders_by_customer(customer_id)
            print("Orders for Customer:")
            for order in orders:
                print(f"- Order ID: {order.order_id}, Total: {order.total_price}")

        elif choice == '8':
            # Exit
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

    # Close the database connection
    db_connection.close_connection()

if __name__ == "__main__":
    main()
