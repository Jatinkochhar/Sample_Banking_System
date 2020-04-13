# import sqlite3 as mysql
# import random as r
# import string
#
# class Account():
#     print("Welcome to AV Bank")
#     def __init__(self,choice):
#         self.choice = choice
#         self.account_number = 0
#         self.header = ('account_holder_name', 'account_number', 'account_balance')
#         #self.account_holder_name = ''
#         self.new_account_balance_deposited = 0
#         #self.mydb = mysql.connect("Bank_Database_Test_1")
#         self.db_cursor = mysql.connect("Bank_Database_Test_1")
#
#     def create_database(self):
#         self.mydb = mysql.connect("Bank_Database_Test_1")
#         self.db_cursor = self.mydb.cursor()
#         self.db_cursor.execute('''CREATE TABLE C12
#                      ( [account_number] INTEGER PRIMARY KEY,[password] text, [account_holder_name] text,[account_balance] integer)''')
#         print(self.db_cursor.rowcount, "Table Created")
#         self.mydb.commit()
#
#     def open_account(self):
#
#         # self.db_cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='C10' ''')
#         # if self.db_cursor.fetchone()[0] == 1:
#         #     print('Table exists.')
#         # else:
#         #     print('Table does not exist.')
#         #     self.db_cursor.execute('''CREATE TABLE C12
#         #                         ( [account_number] INTEGER PRIMARY KEY,[account_holder_name] text,[account_balance] integer)''')
#         #     print(self.db_cursor.rowcount, "Table Created")
#
#
#         # self.db_cursor.execute('''CREATE TABLE C11
#         #                     ( [account_number] INTEGER PRIMARY KEY,[password] text, [account_holder_name] text,[account_balance] integer)''')
#         # print(self.db_cursor.rowcount, "Table Created")
#         #self.mydb.close()
#         self.new_account_holder_name = str(input("Enter new account holder name."))
#         self.account_number = r.randrange(999)
#         print(f"Your acccount account number. It will be your username of your account: {self.account_number}")
#         lettersAndDigits = string.ascii_uppercase + string.digits
#         self.password = ''.join(r.sample(lettersAndDigits, 5))
#         print(f"Your acccount password is: {self.password}")
#
#         self.new_account_deposit = int(input("To open new a/c, deposit minimum Rs.1000/-: "))
#         if self.new_account_deposit>=1000:
#             self.data_inserted = ("INSERT INTO C12(account_number,password,account_holder_name,account_balance) VALUES (?,?,?,?);")
#             self.db_cursor.execute(self.data_inserted, (self.account_number,self.password,self.new_account_holder_name,self.new_account_deposit))
#             self.db_cursor.commit()
#             print(self.db_cursor.rowcount, "record inserted")
#             self.db_cursor.execute("SELECT * FROM C12")
#             result = self.db_cursor.fetchall()
#             for x in result:
#                 print(x)
#
#             print(f"Mr.{self.new_account_holder_name} your a/c has been opened and a/c no. is {self.account_number}, With balance Rs. {self.new_account_deposit}/-")
#
#         else:
#             print("Deposit minimum Rs. 1000/-")
#
#     def existing_holder(self):
#         self.db_cursor.execute("SELECT * FROM C12")
#         result = self.db_cursor.fetchall()
#         for x in result:
#             print(x)
#
#         self.account_number = int(input("Enter account holder number: "))
#         self.holder_password = str(input("Enter password: "))
#         self.db_cursor.execute('SELECT account_holder_name,password, FROM C12 WHERE account_number = ?', [self.account_number])
#         for self.input_password in result[0]:
#             print(self.input_password)
#         self.mydb.commit()
#         result = self.db_cursor.fetchall()
#         for self.account_holder_name_mydb in result[0]:
#             print(self.account_holder_name_mydb)
#         print(f"Welcome Mr.{self.account_holder_name_mydb}. Please select : \nPress 1 deposit money \nPress 2 for withdraw money")
#
#     def deposit(self):
#         self.amount_added = int(input("Enter the amount to be deposited: "))
#         self.db_cursor.execute('SELECT account_balance FROM C12 WHERE account_number = ?', [self.account_number])
#         self.db_cursor.commit()
#         result = self.db_cursor.fetchall()
#         for self.account_balance_mydb in result[0]:
#             print(F"Old balance is : {self.account_balance_mydb}")
#             self.new_account_balance_deposited = self.account_balance_mydb + self.amount_added
#             update_database = ("UPDATE C12 SET account_balance = ? WHERE account_number = ?")
#             self.db_cursor.execute(update_database,(str(self.new_account_balance_deposited), str(self.account_number)))
#             print(f"Mr.{self.account_holder_name_mydb} your new balance is {self.new_account_balance_deposited} of account number {self.account_number}")
#             self.db_cursor.commit()
#
#     def withdraw(self):
#         self.withdraw_money = int(input("Enter amount you want to withdraw: "))
#         self.db_cursor.execute('SELECT account_balance FROM C12 WHERE account_number = ?', [self.account_number])
#         self.db_cursor.commit()
#         result = self.db_cursor.fetchall()
#         for self.account_balance_mydb in result[0]:
#             print(F"Old balance is : {self.account_balance_mydb}")
#         if (self.account_balance_mydb < self.withdraw_money):
#             print("In sufficient balance in account")
#         else:
#             self.new_account_balance_subtracted = self.account_balance_mydb - self.withdraw_money
#             print("Withrawal accepted", self.new_account_balance_subtracted)
#             update_database = ("UPDATE C12 SET account_balance = ? WHERE account_number = ?")
#             self.db_cursor.execute(update_database, (str(self.new_account_balance_subtracted), str(self.account_number)))
#             print(f"Mr.{self.account_holder_name_mydb} your new balance is {self.new_account_balance_subtracted} of account number {self.account_number}")
#             self.db_cursor.commit()
#
#     def __str__(self):
#         return (f"Account Owner: {self.owner} \nAccount Balance: {self.balance}")
#
#
# customer_visit = int(input("Press 1: To Open New Bank Account or Press 2: To Use Existing Account : "))
# acct1 = Account(customer_visit)
# #acct1.create_database()
# if customer_visit ==1:
#     acct1.open_account()
# if customer_visit ==2:
#     acct1.existing_holder()
#     holder_option = int(input())
#     if holder_option ==1:
#         acct1.deposit()
#     if holder_option ==2:
#         acct1.withdraw()
#
# else:
#     print("You have pressed the wrong key, please try again")


#************444444444444444444444444


import sqlite3 as mysql
import random as r
import string
import time

class Account():
    print("Welcome to AV Bank")
    def __init__(self,choice):
        self.choice = choice
        self.account_number = 0
        self.new_account_balance_deposited = 0
        self.mydb = mysql.connect("Bank_Database_Test1")
        self.db_cursor = self.mydb.cursor()

    # def create_database(self):
    #     mydb = mysql.connector.connect(
    #         host="localhost",
    #         user="admin",
    #         passwd="admin",
    #         database="Bank_Database_Test1"
    #     )
    #     db_cursor = mydb.cursor()
    #     db_cursor.execute('''CREATE TABLE CLIENTS
    #                  ( [account_number] INTEGER PRIMARY KEY,[account_holder_name] text,[account_balance] integer)''')
    #     print(db_cursor.rowcount, "Table Created")
    #     mydb.close()

    '''Function to open account. Computer ask account holder name, generates random alpanumeric password. And computer asks to deposit minmum balance'''
    def open_account(self):

        # self.db_cursor.execute('''CREATE TABLE C20
        #                      ( [account_number] INTEGER PRIMARY KEY,[password] text, [account_holder_name] text,[account_balance] integer)''')
        # print(self.db_cursor.rowcount, "Table Created")

        self.new_account_holder_name = str(input("Enter new account holder name: "))
        '''Generate Account Number'''

        self.account_number = r.randrange(999)
        print(f"Your acccount account number. It will be your username of your account: {self.account_number}")

        '''Generate Password'''
        lettersAndDigits = string.ascii_uppercase + string.digits
        self.password = ''.join(r.sample(lettersAndDigits, 5))
        print(f"Your acccount password is: {self.password}")

        '''Input minimum deposit and insert data into database'''
        self.new_account_deposit = int(input("To open new a/c, deposit minimum Rs.1000/-: "))
        if self.new_account_deposit>=1000:
            self.data_inserted = ("INSERT INTO C20 (account_number,password,account_holder_name,account_balance) VALUES (?,?,?,?);")
            self.db_cursor.execute(self.data_inserted, (self.account_number,self.password,self.new_account_holder_name,self.new_account_deposit))
            self.mydb.commit()
            print(f"Mr.{self.new_account_holder_name} your a/c has been opened and a/c no. is {self.account_number}, With balance Rs. {self.new_account_deposit}/-")

        else:
            print(f"Mr.{self.new_account_holder_name} account cannot be open deposit minimum Rs. 1000/-")

    '''Function to verify account holder on basis of username, passoword. If found correct computer will options either to deposit money or withdraw'''
    def existing_holder(self):

        self.db_cursor.execute("SELECT * FROM C20")
        result = self.db_cursor.fetchall()
        for x in result:
            print(x)
        self.input_account_number = int(input("Enter account username : "))


        self.db_cursor.execute('SELECT account_number,password,account_holder_name FROM C20 WHERE account_number = ?', [self.input_account_number])
        self.mydb.commit()
        number = self.db_cursor.fetchall()

        if number == []:
            print("Wrong Username. Account has been locked.Please try after 5 seconds")
            time.sleep(5)
            print("Username has been unlocked. Please try again!!")
            exit()


        else:

            for self.db_number in number:
                password_attempt = 3
                while password_attempt > 0:
                    if self.db_number[0] == self.input_account_number:
                        print("Correct username")
                        self.user_password = str(input("Enter account password: "))
                        if self.db_number[1] == self.user_password:
                                print("Correct password")
                                print(f"Welcome Mr.{self.db_number[2]}.Please select : \nPress 1: Deposit money \nPress 2: Withdraw money")
                                break
                        else:
                            """prompts user for password with every transaction and counterchecks it with stored passwords"""
                            print("\nThat is the wrong password")
                            password_attempt = password_attempt - 1
                            print("%d more attempt(s) remaining" % password_attempt)
                            if password_attempt == 0:
                                print("Account has been locked due to three wrong password attempts,Please try after 10 seconds")
                                time.sleep(10)
                                print("Account has been unlocked. Please try again!!")
                                exit()

                    #exit()
    '''Function to deposit money'''
    def deposit(self):
        self.amount_added = int(input("Enter the amount to be deposited: "))
        self.account_number = self.input_account_number
        self.db_cursor.execute('SELECT * FROM C20 WHERE account_number = ?', [self.account_number])
        self.mydb.commit()
        result = self.db_cursor.fetchall()

        for self.account_balance_mydb in result:
            print(f"Old balance is : {self.account_balance_mydb[3]}")
            self.new_account_balance_deposited = self.account_balance_mydb[3] + self.amount_added
            update_database = ("UPDATE C20 SET account_balance = ? WHERE account_number = ?")
            self.db_cursor.execute(update_database,(str(self.new_account_balance_deposited), str(self.account_number)))
            self.mydb.commit()
            print(f"Mr.{self.account_balance_mydb[2]} your new balance is {self.new_account_balance_deposited} of account number {self.account_number}")

    """Function to withdraw money"""
    def withdraw(self):
        self.withdraw_money = int(input("Enter amount you want to withdraw: "))
        self.account_number = self.input_account_number
        self.db_cursor.execute('SELECT * FROM C20 WHERE account_number = ?', [self.account_number])
        self.mydb.commit()
        result = self.db_cursor.fetchall()
        print(result)
        for self.account_balance_mydb in result:
            print(f"Previous account balance is : {self.account_balance_mydb[3]}")
            if (self.account_balance_mydb[3] < self.withdraw_money):
                print("In sufficient balance in account")
                break
            else:
                self.new_account_balance_subtracted = self.account_balance_mydb[3] - self.withdraw_money
                print("Withrawal accepted. New balance is :", self.new_account_balance_subtracted)

            update_database = ("UPDATE C20 SET account_balance = ? WHERE account_number = ?")
            self.db_cursor.execute(update_database, (str(self.new_account_balance_subtracted), str(self.account_number)))
            self.mydb.commit()
            print(f"Mr.{self.account_balance_mydb[2]} your new balance is {self.new_account_balance_subtracted} of account number {self.account_number}")

    def __str__(self):
        return (f"Account Owner: {self.owner} \nAccount Balance: {self.balance}")


customer_visit = int(input("Press 1: To Open New Bank Account or Press 2: To Use Existing Account : "))
acct1 = Account(customer_visit)

if customer_visit ==1:
    acct1.open_account()
elif customer_visit ==2:
    acct1.existing_holder()
    holder_option = int(input("Enter Option: "))
    if holder_option ==1:
        acct1.deposit()
    elif holder_option ==2:
        acct1.withdraw()
    else:
         print("Enter either 1 or 2")
else:
     print("Enter either 1 or 2")