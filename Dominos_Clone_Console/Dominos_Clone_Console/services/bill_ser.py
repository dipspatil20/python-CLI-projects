class BillService:
    def display_bill(self, order):
        print("\n----- BILL -----")
        for item, qty in order.items:
            print(f"{item.name} x{qty} = ₹{item.price * qty}")
        print(f"Total: ₹{order.get_total()}")
        print("---------------\n")
