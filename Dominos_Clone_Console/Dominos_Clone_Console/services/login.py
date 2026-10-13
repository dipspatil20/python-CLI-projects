import sqlite3 as sql
from register import Register as reg

class LoginError(Exception):
    pass

class Login(reg):
    con = sql.connect('Dominos')
    part = con.cursor()

    @classmethod
    def log(cls, us, pw):
        username, password = reg.reg()

        if username == us:
            if password == pw:
                print('Login Successful')
            else:
                print('Wrong password...')
                raise LoginError
        else:
            print('Wrong username...')
            raise LoginError
