from models.order import Order

class OrderService:
    def __init__(self, db_manager):
        self.db = db_manager

    def create_order(self, customer_id):
        return Order(None, customer_id)

    def add_to_cart(self, order, menu_item, quantity):
        order.add_item(menu_item, quantity)
