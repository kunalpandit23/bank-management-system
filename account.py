# create/update account

import json
import random


class Account():
    def __init__(self):
        self.Customer = {}

    def CreateNewAccount(self):
        while True:
            print("----------------------------------------------------------")
            print("         Enter all the following details")
            print("----------------------------------------------------------")

            Acc_No = random.randint(100000000000, 999999999999)
            
            try:
                with open("db/customers.json", "r") as file:
                    self.Customer = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                self.Customer = {}  # If file doesn't exist, start fresh               

            if Acc_No not in self.Customer:
                self.Customer[Acc_No] = {}

            print("----------------------------------------------------------")
            name = input("Enter Account Holder Full Name: ").strip().upper()
            print("----------------------------------------------------------")
            password= input("Create Password: ").strip()
            print("----------------------------------------------------------")

            while True:
                try: 
                    print("----------------------------------------------------------")
                    balance = int(input("Add minimum 500₹ deposit: "))
                    print("----------------------------------------------------------")

                    if balance < 500:
                        raise Exception("Amount is less than 500₹ please add minimum 500₹")
                    else:
                        break
                except Exception as e:
                    print("----------------------------------------------------------")
                    print(f"      {e}")
                    print("----------------------------------------------------------")

            print("----------------------------------------------------------")
            email = input("Enter Email: ").strip().upper()
            print("----------------------------------------------------------")
            mobile = int(input("Enter Mobile No: "))
            print("----------------------------------------------------------")


            self.Customer[Acc_No]["Account No"] = Acc_No
            self.Customer[Acc_No]["Name"] = name
            self.Customer[Acc_No]["Password"] = password
            self.Customer[Acc_No]["Balance"] = balance
            self.Customer[Acc_No]["Email"] = email
            self.Customer[Acc_No]["Mobile No"] = mobile

            print("----------------------------------------------------------")
            confirm = input("Check All information are Correct then Confirm (yes/no): ").strip().lower()
            print("----------------------------------------------------------")

            
            if confirm == "yes":
                with open("db/customers.json", "w") as file:
                    json.dump(self.Customer, file, indent=4)
                    break
            else:
                print("----------------------------------------------------------")
                print("         Some Thing Else Wrong.(Try Again) ")
                print("----------------------------------------------------------")
                break



            
