# create/update account

import json
import random


class Account():
    def __init__(self):
        self.Customer = {}

    def CustomerInfo(self):
        while True:
            print("\nEnter all the following details")
            Acc_No = random.randint(100000000000, 999999999999)
            
            try:
                with open("db/customers.json", "r") as file:
                    self.Customer = json.load(file)
            except FileNotFoundError:
                self.Customer = {}  # If file doesn't exist, start fresh               

            if Acc_No not in self.Customer:
                self.Customer[Acc_No] = {}

            name = input("\nEnter Account Holder Full Name: ")
            password= input("\nCreate Password: ")
            balance = input("\nAdd minimum 500rs deposit: ")
            email = input("\nEnter Email: ")
            mobile = int(input("\nEnter Mobile No: "))

            self.Customer[Acc_No]["Account No"] = Acc_No
            self.Customer[Acc_No]["Name"] = name
            self.Customer[Acc_No]["Password"] = password
            self.Customer[Acc_No]["Balance"] = balance
            self.Customer[Acc_No]["Email"] = email
            self.Customer[Acc_No]["Mobile No"] = mobile

            another_input = input("\nAdd another account (yes/no)")
            if another_input != "yes":
                break

        with open("db/customers.json", "w") as file:
            json.dump(self.Customer, file, indent=4)

            

# a = Account()

# a.CustomerInfo()
# a.SaveInfo()
