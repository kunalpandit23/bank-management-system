
from auth import Auth

class Main(Auth):

    def main_dashboard(self):
            print("----------------------------------------------------------")        
            print("1. Login.\n2. Sign Up\n3. Exit")
            print("----------------------------------------------------------")

            user_input = input("").strip().lower()

            if user_input in ["login", "1"]:
                print("----------------------------------------------------------")
                print("1. Admin Login.\n2. Customer Login\n3. Exit")
                print("----------------------------------------------------------")

                another_input = input("").strip().lower()

                if another_input in ["admin","admin login", "1"]:
                    self.Admin_login()

                elif another_input in ["customer","customer login", "2"]:
                    self.customer_login()

                else:
                    print("----------------------------------------------------------")
                    print("         INVALID INPUT")
                    print("----------------------------------------------------------")

            elif user_input in ["signup", "2"]:
                self.signup_account()

                  
            elif user_input in ["exit","3"]:
                print("----------------------------------------------------------")
                print("         Successfully Exited")
                print("----------------------------------------------------------")
                

m = Main()

m.main_dashboard()