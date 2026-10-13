# Dominos mini project

class Dominos:

    def __init__(self, name, phone, addr, cart=[], bill=0):
        self.name = name
        self.phone = phone
        self.address = addr
        self.cart = cart
        self.bill = bill

    pizza = {'veggie-piz':150, 'chicken-piz':350, 'corn-piz':200, 'mix-veg-piz':250}
    burger = {'veggie-bg':150, 'chicken-bg':250, 'jumbo veg-bg':300, 'jumbo chicken-bg':350}
    sides = {'breadstick':50, 'garlic-breadstick':100, 'cheese-breadstick':80, 'lava cake':80}
    apptizers = {'sprite':60, 'coke':60, 'cold coffe':130, 'hot chocolate':100, 'oreo-shake':120}

    @classmethod
    def disp_menu(cls):
        while True:
            print('''Enter 1 for Pizza: 
                    Enter 2 for Burgers: 
                    Enter 3 for sides: 
                    Enter 4 for appetizers: 
                    Enter 5 to exit Menu...''')
            n = int(input('Enter your choice of Menu: '))
            print('Item     Price')
            if n == 1:
                for i,j in cls.pizza.items():
                    print(i, j)
            elif n == 2:
                for i,j in cls.burger.items():
                    print(i, j)
            elif n == 3:
                for i,j in cls.sides.items():
                    print(i, j)
            elif n == 4:
                for i,j in cls.apptizers.items():
                    print(i, j)
            elif n == 5:
                break
            else:
                print('Invalid input...')
    

    @staticmethod
    def add(m,n,food):
        return m + food.get(n)
    

    def order(self):
        while True:
            print('''Enter 1 for Pizza: 
                    Enter 2 for Burgers: 
                    Enter 3 for sides: 
                    Enter 4 for appetizers: 
                    Enter 5 to end the order...''')
            n = int(input('Enter your choice of Food: '))
            if n == 1:
                item = input('Enter the item: ')
                self.cart.append(item)
                self.bill = self.add(self.bill,item,self.pizza)
            elif n == 2:
                item = input('Enter the item: ')
                self.cart.append(item)
                self.bill = self.add(self.bill,item,self.burger)
            elif n == 3:
                item = input('Enter the item: ')
                self.cart.append(item)
                self.bill = self.add(self.bill,item,self.sides)
            elif n == 4:
                item = input('Enter the item: ')
                self.cart.append(item)
                self.bill = self.add(self.bill,item,self.apptizers)
            elif n == 5:
                break
            else:
                print('Invalid input...')
    

    def view_cart(self):
        for i in self.cart:
            print(i)


    def view_bill(self):
        print("Total order amount: ", self.bill)
    