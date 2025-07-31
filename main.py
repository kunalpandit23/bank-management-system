from admin_panel import Admin
from customer_dashboard import Customer
from account import Account
import os

class Main(Admin, Customer, Account):

    def main_dashboard(self):
        
            print("\n1. Login.\n2. Sign Up\n3. Exit")
            user_input = input("")

            if user_input == "login" or user_input == "1":
                print("\n1. Admin Login.\n2. Customer Login\n3. Exit")
                another_input = input("")

                if another_input == "admin" or another_input == "1":
                    main.Admin_login()

                elif another_input == "customer" or another_input == "2":
                    main.my_account()

                else:
                    print("\nINVALID INPUT...")

            elif user_input == "signup" or user_input == "2":
                main.CustomerInfo()

                    
            elif user_input == "exit" or user_input == "3":
                print("\nExit successfully... ")
                





main = Main()

main.main_dashboard()