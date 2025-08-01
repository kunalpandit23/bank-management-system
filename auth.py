# login/signup
import json
from admin_panel import Admin
from customer_dashboard import Customer
from account import Account

class Auth(Admin, Customer, Account):
    def Admin_login(self):
        print("----------------------------------------------------------")
        print("1. Login\n2. Forgot Password")
        print("----------------------------------------------------------")

        user_input = input()

        try:
            with open("db/admin.json", 'r') as file:
                self.AdminInfo = json.load(file)

        except FileNotFoundError:
                self.AdminInfo = {}

        if user_input == "login" or user_input == "1":
            print("----------------------------------------------------------")
            id = input("Enter your Admin ID: ").strip()
            password = input("\nEnter your Password: ").strip()
            print("----------------------------------------------------------")
        

            if id == self.AdminInfo["Admin1"]["ID"] and password == self.AdminInfo["Admin1"]["Password"]:
                print("----------------------------------------------------------")
                print("         Login successfully completed")
                print("----------------------------------------------------------")
                self.admin_options()

            else:
                print("----------------------------------------------------------")
                print("         Account Not Found")
                print("----------------------------------------------------------")

        


    def customer_login(self):
            with open("db/customers.json", 'r') as file:
                    self.data = json.load(file)
            print("----------------------------------------------------------")
            self.Acc_no = input("Enter your Account Number: ")
            self.password = input("Enter your password: ")
            print("----------------------------------------------------------")
            
            if self.data.get(self.Acc_no) and self.password == self.data[self.Acc_no]["Password"]:
                print("----------------------------------------------------------")
                print("         Login successfully completed")
                print("----------------------------------------------------------")
                self.customer_options()

            else:
                print("----------------------------------------------------------")
                print("\n           Account Not Found")
                print("----------------------------------------------------------")

    def signup_account(self):
         self.CreateNewAccount()

