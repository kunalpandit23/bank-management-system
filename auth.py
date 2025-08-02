# login/signup
import json
from json.decoder import JSONDecodeError
from admin_panel import AdminMenu
from customer_dashboard import CustomerMenu
from account import Account

class Auth(AdminMenu, CustomerMenu, Account):
    def Admin_login(self):
        print("----------------------------------------------------------")
        print("1. Login\n2. Forgot Password")
        print("----------------------------------------------------------")

        user_input = input()

        try:
            with open("db/admin.json", 'r') as file:
                self.AdminInfo = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            self.AdminInfo = {}

        if user_input == "login" or user_input == "1":
            print("----------------------------------------------------------")
            id = input("Enter your Admin ID: ").strip()
            password = input("\nEnter your Password: ").strip()
            print("----------------------------------------------------------")
        

            admin = self.AdminInfo.get("Admin1")
            if admin and id == admin.get("ID") and password == admin.get("Password"):
                print("----------------------------------------------------------")
                print("         Login successfully completed")
                print("----------------------------------------------------------")
                self.admin_options()

            else:
                print("----------------------------------------------------------")
                print("         Account Not Found")
                print("----------------------------------------------------------")

        


    def customer_login(self):
            try:
                with open("db/customers.json", 'r') as file:
                    self.data = json.load(file)
            except (FileNotFoundError, JSONDecodeError):
                self.data = {}

            print("----------------------------------------------------------")
            self.Acc_no = input("Enter your Account Number: ")
            self.password = input("Enter your password: ")
            print("----------------------------------------------------------")

            customer = self.data.get(self.Acc_no)
            if customer and self.password == customer.get("Password"):
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
