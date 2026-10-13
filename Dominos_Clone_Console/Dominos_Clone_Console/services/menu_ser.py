class MenuService:
    def __init__(self, db_manager):
        self.db = db_manager

    def display_menu(self):
        menu_items = self.db.get_all_menu_items()
        print("\n--- MENU ---")
        for item in menu_items:
            print(f"{item.item_id}: {item.name} - ₹{item.price} ({item.description})")
        print()
        return menu_items
