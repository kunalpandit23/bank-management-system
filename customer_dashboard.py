import json
from account import Account

class Customer(Account):

    def my_account(self):       
        with open("db/customers.json", 'r') as file:
            data = json.load(file)

        Acc_no = input("\nEnter your Account Number: ")
        password = input("\nEnter your password: ")

        if Acc_no in data and password == data[Acc_no]["Password"]:
            print("\nLogin successful...")

            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")  
            another_input = input()      

            if another_input == "deposit" or another_input == "1":
                c.deposit()
            elif another_input == "withdraw" or "2":
                c.withdraw()
            elif another_input == "checkbalance" or "3":
                c.view_balance()
            else:
                print("\nINVALID INPUT...")
        else:
            print("\nInvalid Account No or Password")
       
    def deposit(self):
        print("deposit successfully...")
        
    def withdraw(self):
        print("withdraw successfully...")

    def view_balance(self):
        print("view balance successfully...")

    def fund_transfer(self):
        pass

    def view_statement(self):
        pass

    def update_details(self):
        pass

    def close_account(self):
        pass

    def ExitToMainMenu(self):
        pass
            
c = Customer()

