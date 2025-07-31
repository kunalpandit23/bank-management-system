import json

class Admin:
    def __init__(self):
     self.AdminInfo = {}

    def Admin_login(self):
        print("\n1. Login with ID & Password \n2. Forgot ID & Password\n")
        user_input = input()
        try:
            with open("db/admin.json", 'r') as file:
                self.AdminInfo = json.load(file)

        except FileNotFoundError:
                self.AdminInfo = {}

        if user_input == "login" or user_input == "1":
            id = input("\nEnter your Admin ID: ").strip()
            password = input("\nEnter your Password: ").strip()

            if id == self.AdminInfo["Admin1"]["ID"] and password == self.AdminInfo["Admin1"]["Password"]:
                print("\nAdmin login successfully...")
                while True:
                    print("\n1. View All Account\n2. Search Account\n3. Delete Account\n4. Check Total Bank Balance\n5. Exit")
                    another_input = input()

                    if another_input in ["viewaccount", "1"]:
                        self.ViewAllAccount()                   
                    elif another_input in ["searchaccount", "2"]:
                        self.SearchAccount()
                    elif another_input in ["deleteaccount", "3"]:
                        self.DeleteAccount()
                    elif another_input in ["check total bank balance", "4"]:
                        self.TotalBankBalance()
                    elif another_input in ["exit", "5"]:
                        break
                    else:                   
                        print("\nINVALID INPUT...")

            else:
                print("\nInvalid ID, Password.")

        elif user_input in ["forgotpassword", "forgot password", "forgot", "2"]:
            if "Admin1" not in self.AdminInfo:
                self.AdminInfo["Admin1"] = {}


            print("Tell mi some answers")
            name = input("Tell mi your name : ").upper().strip()

            if name == self.AdminInfo["Admin1"]["Name"]:
                print("correct answer")
                new_ID = input("Create new Id: ").strip()
                new_password = input("Create new password : ").strip()

                self.AdminInfo["Admin1"]["ID"] = new_ID
                self.AdminInfo["Admin1"]["Password"] = new_password

            else:
                print("You are not Admin ")
            
            with open("db/admin.json", 'w') as file:
                json.dump(self.AdminInfo, file, indent=4)

        else:
            print("INVALID INPUT")
        
    
    def ViewAllAccount(self):

        with open("db/customers.json", 'r') as file:
            data = json.load(file)

        for acc, details in data.items():
            print(f"Account No : {acc}")
            print(f"Name : {details["Name"]}")
            print(f"Password : {details["Password"]}")
            print(f"Balance: {details["Balance"]}₹")
            print(f"Email: {details["Email"]}")
            print(f"Mobile No: {details["Mobile No"]}")
            print("-" * 40)      

    def SearchAccount(self):
        with open("db/customers.json", 'r') as file:
            data = json.load(file)

        while True:           
            print("Enter Customer Account No.")
            acc_no = input()

            if acc_no in data:           
                name = data[acc_no]["Name"]
                password = data[acc_no]["Password"]
                balance = data[acc_no]["Balance"]
                email = data[acc_no]["Email"]
                mobile_no = data[acc_no]["Mobile No"]

                print("-" * 40)   
                print(f"Account No : {acc_no}")
                print(f"Name : {name}")
                print(f"Password : {password}")
                print(f"Balance: {balance}₹")
                print(f"Email: {email}")
                print(f"Mobile No: {mobile_no}")
                print("-" * 40)   
            else:
                print("Account Not Fount")

            another_input = input("Check Another Account (yes/no): ").strip().lower()
            if another_input != "yes":
                break


    def DeleteAccount(self):
        with open("db/customers.json", 'r') as file:
            data = json.load(file)

        print("Enter Account Number ")
        acc = input()

        if acc in data:
            confirm = input("Confirm delete Account(yes/no) ").strip().lower()
            if confirm == "yes":
                del data[acc]
                print("Account successfully Deleted")
                with open("db/customers.json", 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                print("Account delete process Canceled...")
        else:
            print("Account Not Found")


    def TotalBankBalance(self):
        with open("db/customers.json", 'r') as file:
            self.data = json.load(file)
        total = 0
        for acc, details in self.data.items():
            acc
            total += details["Balance"] 
        print(f" _______________________________________")
        print(f"|                                       |")
        print(f"|    Total Bank Balance: {total}₹         |")
        print(f"|_______________________________________|")

     
    def ViewAllTransaction(self):
        pass            
    
    def ExitToMainMenu(self):
        pass
a = Admin()

# a.Admin_login()
# a.ViewAllAccount()
# a.SearchAccount()
# a.DeleteAccount()
# a.TotalBankBalance()