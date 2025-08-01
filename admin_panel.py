import json

class Admin:
    def __init__(self):
     self.AdminInfo = {}

    def ViewAllAccount(self):

        with open("db/customers.json", 'r') as file:
            data = json.load(file)

        for acc, details in data.items():
            print("----------------------------------------------------------") 
            print(f"Account No          : {acc}")
            print(f"Account Holder Name : {details["Name"]}")
            print(f"Password            : {details["Password"]}")
            print(f"Balance             : {details["Balance"]}₹")
            print(f"Email               : {details["Email"]}")
            print(f"Mobile No           : {details["Mobile No"]}")
            print("----------------------------------------------------------")
                 

    def SearchAccount(self):
        with open("db/customers.json", 'r') as file:
            data = json.load(file)

        while True:           
            print("----------------------------------------------------------")
            acc_no = input("Enter Customer Account No: ")
            print("----------------------------------------------------------")


            if acc_no in data:           
                name = data[acc_no]["Name"]
                password = data[acc_no]["Password"]
                balance = data[acc_no]["Balance"]
                email = data[acc_no]["Email"]
                mobile_no = data[acc_no]["Mobile No"]

                print("----------------------------------------------------------")  
                print(f"Account No          : {acc_no}")
                print(f"Account Holder Name : {name}")
                print(f"Password            : {password}")
                print(f"Balance             : {balance}₹")
                print(f"Email               : {email}")
                print(f"Mobile No           : {mobile_no}")
                print("----------------------------------------------------------")

            else:
                print("----------------------------------------------------------")
                print("         Account Not Fount")
                print("----------------------------------------------------------")

            print("----------------------------------------------------------")
            another_input = input("Search Another Account (yes/no): ").strip().lower()
            print("----------------------------------------------------------")

            if another_input != "yes":
                break


    def DeleteAccount(self):
        with open("db/customers.json", 'r') as file:
            data = json.load(file)
        print("----------------------------------------------------------")
        acc = input("Enter Account Number: ")
        print("----------------------------------------------------------")


        if acc in data:
            print("----------------------------------------------------------")
            confirm = input("Confirm delete Account(yes/no) ").strip().lower()
            print("----------------------------------------------------------")

            if confirm == "yes":
                del data[acc]
                print("----------------------------------------------------------")
                print("         Account successfully Deleted")
                print("----------------------------------------------------------")

                with open("db/customers.json", 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                print("----------------------------------------------------------")
                print("         Account delete process Canceled")
                print("----------------------------------------------------------")

        else:
            print("----------------------------------------------------------")
            print("         Account Not Found")
            print("----------------------------------------------------------")



    def TotalBankBalance(self):
        with open("db/customers.json", 'r') as file:
            self.data = json.load(file)
        total = 0
        for acc, details in self.data.items():
            acc
            total += details["Balance"] 
        print("----------------------------------------------------------")
        print(f"        Total Bank Balance: {total}₹         ")
        print("----------------------------------------------------------")


     
    def ViewAllTransaction(self):
        pass            
    
    def ExitToMainMenu(self):
        pass

class AdminMenu(Admin):

    def admin_options(self):
        while True:
            print("----------------------------------------------------------")    
            print("1. View All Account\n2. Search Account\n3. Delete Account\n4. Check Total Bank Balance\n5. Exit")
            print("----------------------------------------------------------")

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
                print("----------------------------------------------------------")
                print("         Successfully Exited")
                print("----------------------------------------------------------")

                break
            else: 
                print("----------------------------------------------------------")
                print("         INVALID INPUT")
                print("----------------------------------------------------------")

            print("----------------------------------------------------------")
            another_input = input("Perform another action? (yes/no): ").strip().lower()
            print("----------------------------------------------------------")

            if another_input != "yes":
                break
 
