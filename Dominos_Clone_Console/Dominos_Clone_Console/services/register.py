import sqlite3
class Register:

    def __init__(self, name, phone, addr, cart=[], bill=0):
        self.name = name
        self.phone = phone
        self.address = addr
        self.cart = cart
        self.bill = bill

    @staticmethod
    def reg():
        username = input('Enter Username for registration: ')
        password = input('Enter password for registration: ')
        return username, password