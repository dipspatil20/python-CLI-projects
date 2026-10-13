from database.db_manager import DBManager

class AuthService:
    def __init__(self, db_manager):
        self.db = db_manager

    def signup(self, name, email, password):
        self.db.add_customer(name, email, password)

    def login(self, email, password):
        customer = self.db.get_customer_by_email(email)
        if customer and customer.password == password:
            return customer
        return None
