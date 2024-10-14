import pyodbc

class DBConnection:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            try:
                # Replace with your actual server and database details
                self.connection = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=DESKTOP\SQLEXPRESS;'  # Use your server name if different
                    'DATABASE=projectdb;'  # Replace with your database name
                    'Trusted_Connection=yes;'  # Use Windows Authentication
                )
                print("Database connection established.")
            except Exception as e:
                print(f"Error connecting to database: {e}")
                self.connection = None
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
