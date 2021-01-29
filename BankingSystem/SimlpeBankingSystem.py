# imports
import random
import sqlite3


# Create a Class account
class Account:

    def __init__(self):

        self.iin = '400000'
        self.balance = 0
        self.card_num = ''
        self.card_pin = ''

    # create an account and check with Luhn algorithm
    def create_account(self):
        card_num = []
        card_pin = []
        checksum = '0'
        for _ in range(9):
            card_num.append(str(random.randint(0, 9)))

        # check the validity with Luhn
        iin = [int(x) for x in self.iin]
        num_to_check = iin + [int(x) for x in card_num]
        for i in range(0, len(num_to_check), 2):
            num_to_check[i] *= 2
        for i in range(len(num_to_check)):
            if num_to_check[i] > 9:
                num_to_check[i] -= 9
        sum_of_num = sum(num_to_check)
        # find checksum
        if sum_of_num % 10 == 0:
            checksum = '0'
        else:
            checksum = str(10 - (sum_of_num % 10))
        self.card_num = self.iin + ''.join(card_num) + checksum
        for i in range(4):
            card_pin.append((str(random.randint(0, 9))))
        self.card_pin = ''.join(card_pin)

        self.check_db()

    # method for creating database
    def create_db(self):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS card (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    number TEXT,
                    pin TEXT,
                    balance INT DEFAULT 0 );""")
        conn.commit()

    # method to add data to database
    def add_to_db(self):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute('INSERT INTO card VALUES (1, ?, ?, ?)', (self.card_num, self.card_pin, self.balance))
        conn.commit()

    # add data to db if not empty
    def update_db(self):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute("""INSERT INTO card (number, pin, balance) VALUES(?, ?, ?)""", (self.card_num, self.card_pin, self.balance))
        conn.commit()

    # check the database whether empty and adds data into
    def check_db(self):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM card')
        rows = cur.fetchall()
        if len(rows) == 0:
            self.add_to_db()
        else:
            self.update_db()
            conn.commit()
    # get balance
    def get_balance(self):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute("SELECT balance FROM card WHERE (number = ?)", (self.card_num,))
        balance = cur.fetchone()
        self.balance = balance[0]
        return(self.balance)
        conn.commit()

    # get all data from database
    def get_from_db(self):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM card')
        data = cur.fetchall()
        return data
        conn.commit()

    # update the balance when the amount is put
    def add_amount(self):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute("SELECT balance FROM card WHERE (number = ?)", (self.card_num,))
        balance = cur.fetchone()[0]
        mess = input('Enter income:\n')
        balance += int(mess)
        cur.execute("""UPDATE card SET balance = ? WHERE number = ? """, (balance, self.card_num))
        print("The balance updated!\n")
        conn.commit()

    # transfer from one account to another
    def transfer(self):
        data = self.get_from_db()
        card_nums = [i[1] for i in data]
        print('Transfer')

        trans_card = input('Enter card number:\n')
        # check one more time with Luhn
        check_num = [int(x) for x in trans_card]
        checksum = check_num[-1]
        luhn_check = check_num[:-1]
        # multiply odds positions by 2
        for i in range(0, len(luhn_check), 2):
            luhn_check[i] *= 2
        # substract 9 tu numbers over 9
        for i in range(len(luhn_check)):
            if luhn_check[i] > 9:
                luhn_check[i] -= 9
        sum_numb = sum(luhn_check) + checksum
        if sum_numb % 10 != 0:
            print('Probably you made a mistake in the card number. Please try again!\n')
        elif trans_card == self.card_num:
            print('You can\'t transfer money to the same account!\n')
        elif trans_card not in card_nums:
            print('Such a card does not exist.\n')
        else:
            trans_money = input('Enter amount you want to transfer:\n')
            self.balance = self.get_balance()
            if int(trans_money) > int(self.balance):
                print('Not enough money!\n')
            else:
                conn = sqlite3.connect("card.s3db")
                cur = conn.cursor()
                cur.execute('SELECT balance FROM card WHERE (number = ?)', (trans_card,))
                balance = cur.fetchone()[0]
                balance += int(trans_money)
                cur.execute('''UPDATE card SET balance = ? WHERE number = ? ''', (balance, trans_card))
                print('Success!\n')
                cur.execute('SELECT balance FROM card WHERE (number = ?)', (self.card_num,))
                updated_balance = int(cur.fetchone()[0]) - int(trans_money)
                cur.execute('''UPDATE card SET balance = ? WHERE number = ? ''', (updated_balance, self.card_num))
                conn.commit()

    # delete account from database
    def del_account(self):
        conn = sqlite3.connect("card.s3db")
        cur = conn.cursor()
        cur.execute('DELETE FROM card WHERE (number = ?)', (self.card_num,))
        print('The account has been deleted!\n')
        conn.commit()

    # take user input and do tasks accordingly
    def main(self):
        self.create_db()
        while True:
            menu = input("1. Create an account\n2. Log into account\n0. Exit\n")
            if menu == '1':
                self.create_account()

                print(f"\nYour card has been created\n\Your card number:\n{self.card_num}\nYour card PIN:\n{self.card_pin}\n")
            elif menu == '2':
                card_num = input('\nEnter your card number:\n')
                card_pin = input('Enter your PIN:\n')
                self.card_num = card_num
                self.card_pin = card_pin
                data = self.get_from_db()
                mess = ''
                card_nums = []
                for i in data:
                    card_nums.append(i[1])
                    if card_num in i and card_pin in i:
                        mess = '\nYou have successfully logged in!\n'
                        print(mess)
                        break
                else:
                    print('\nWrong card number or PIN!\n')
                if len(mess) > 1:
                    submenu = ''
                    while submenu != 0:
                        submenu = input("1. Balance\n2. Add income\n3. Do transfer\n\4. Close account\n5. Log out\n0. Exit\n")
                        if submenu == '1':
                            print(f'\nBalance: {self.get_balance()}\n')
                            self.balance = self.get_balance()
                            continue
                        elif submenu == '2':
                            self.add_amount()
                            continue
                        elif submenu == '3':
                            self.transfer()
                            continue
                        elif submenu == '4':
                            self.del_account()
                            break
                        elif submenu == '5':
                            print('\nYou have successfully logged out!\n')
                            break
                        else:
                            if submenu == '0':
                                print('\nBye!\n')
                                exit()
                        break
            else:
                if menu == '0':
                    print('\nBye!')
                    break

account = Account()
Account.main(account)