from database.db_manager import DBManager
from services.authorization import AuthService
from services.menu_ser import MenuService
from services.order_ser import OrderService
from services.bill_ser import BillService


def main():
    db = DBManager()
    auth = AuthService(db)
    menu = MenuService(db)
    order_ = OrderService(db)
    bill = BillService()

    # Example flow: signup, login, display menu, order, view cart, display bill
    # (Implement CLI or UI as needed)

    if not db.get_all_menu_items():
        db.add_menu_item("Margheritta", 129, "Classical Cheese Pizza")
        db.add_menu_item("Farmhouse veggie", 249, "Fully loaded veg Pizza")
        db.add_menu_item("Mushroom magic", 199, "Mushroom loaded Pizza")
        db.add_menu_item("Chickennn", 199, "Chicken Pizza")
        db.add_menu_item("Hornie-Cornie", 149, "Golden corn loaded pizza")
        db.add_menu_item("Vampire Killer Sticks", 119, "Garlic Sticks")
        db.add_menu_item("Coke", 89, "Cocacola")
        db.add_menu_item("Choco Fountain", 159, "Hot Chocolate Syrup")

    print("Welcome To Dominos Pizza Clone application...")

    while True:
        try:
            print('''1. Sign-up\n2. Login\n3. Exit''')
            n = int(input("Enter your choice: "))
            if n == 1:
                name = input('Enter your name: ')
                email = input('Enter you Email: ')
                password = input('Enter your password: ')
                auth.signup(name, email, password)
                print("Signup is Successful...")
            elif n == 2:
                email = input('Enter your  Email: ')
                password = input('Enter your password: ')
                cust = auth.login(email, password)
                if cust:
                    print(f'''Login Successful...
                          Welcome {cust.name}''')
                    order = order_.create_order(cust.customer_id)
                    while True:
                        print('''1. Show Menu\n2. Add to Cart\n3. View Cart\n4. Display Bill\n5. Logout''')
                        print("-----------------------------------------------------------------------------------------------")
                        try:
                            inp = int(input("Enter your choice: "))
                            if inp == 1:
                                menu.display_menu()
                                print("-----------------------------------------------------------------------------------------------")
                            elif inp == 2:
                                items = menu.display_menu()
                                items_id = int(
                                    input('Enter item ID to add to cart: '))
                                qty = int(input('Enter Quantity: '))
                                sel = next(
                                    (i for i in items if i.item_id == items_id), None)

                                if sel:
                                    order_.add_to_cart(order, sel, qty)
                                    print(
                                        f"Added {sel.name} X {qty} to cart...")
                                    print("-----------------------------------------------------------------------------------------------")
                                else:
                                    print("Invalid Item ID...")
                            elif inp == 3:
                                print("\n--- CART ---")
                                for i, j in order.items:
                                    print(f"{i.name} X {j} = ₹{i.price * j}")
                                print("-----------------------------------------------------------------------------------------------")
                            elif inp == 4:
                                bill.display_bill(order)
                                print("-----------------------------------------------------------------------------------------------")
                            elif inp == 5:
                                print("Logged Out.\n")
                                print("-----------------------------------------------------------------------------------------------")
                                break
                            else:
                                print('Invalid choice...')

                        except ValueError:
                            print("Kindly enter only number as your choice...")
                else:
                    print("Login failed, kindly signup first...")
            elif n == 3:
                print("Happy to serve...\n--- GOODBYE ---")
                print("-----------------------------------------------------------------------------------------------")
                break
            else:
                print("Enter a valid input...")

        except ValueError:
            print("Kindly enter only number as your choice...")


if __name__ == "__main__":
    main()
