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

            name = input("\nEnter Account Holder Full Name: ").strip().upper()
            password= input("\nCreate Password: ").strip()
            while True:
                try: 
                    balance = int(input("\nAdd minimum 500₹ deposit: "))
                    if balance < 500:
                        raise Exception("Amount is less than 500₹ please add minimum 500₹")
                    else:
                        break
                except Exception as e:
                    print(e)
            email = input("\nEnter Email: ").strip()
            mobile = int(input("\nEnter Mobile No: "))

            self.Customer[Acc_No]["Account No"] = Acc_No
            self.Customer[Acc_No]["Name"] = name
            self.Customer[Acc_No]["Password"] = password
            self.Customer[Acc_No]["Balance"] = balance
            self.Customer[Acc_No]["Email"] = email
            self.Customer[Acc_No]["Mobile No"] = mobile

            confirm = input("Check All information are Correct then Confirm (yes/no): ").strip().lower()
            
            if confirm == "yes":
                with open("db/customers.json", "w") as file:
                    json.dump(self.Customer, file, indent=4)
                    break
            else:
                print("Account Not Created.(Try again) ")
                break



            

# a = Account()

# a.CustomerInfo()
# a.SaveInfo()
