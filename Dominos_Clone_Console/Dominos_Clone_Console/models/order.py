class Order:
    def __init__(self, order_id, customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = []  # List of (MenuItem, quantity) tuples

    def add_item(self, menu_item, quantity):
        self.items.append((menu_item, quantity))

    def get_total(self):
        return sum(item.price * qty for item, qty in self.items)
