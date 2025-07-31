import json
from account import Account

class Customer(Account):

    def my_account(self):
        with open("db/customers.json", 'r') as file:
                self.data = json.load(file)

        self.Acc_no = input("\nEnter your Account Number: ")
        self.password = input("\nEnter your password: ")
         
        if self.data.get(self.Acc_no) and self.password == self.data[self.Acc_no]["Password"]:
            print("\nLogin successful...")

            while True:       
                print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Close Account\n5. Exit")
                another_input = input().strip().lower()      

                if another_input in ["deposit", "1"]:
                    self.deposit()
                elif another_input in ["withdraw", "2"]:
                    self.withdraw()
                elif another_input in ["check balance","checkbalance", "3"]:
                    self.view_balance()
                elif another_input in ["close account", "checkaccount", "4"]:
                    self.close_account()
                    break
                elif another_input in ["exit", "5"]:
                    self.ExitToMainMenu()
                    print("Exit Successful")
                    break
                else:
                    print("\nINVALID INPUT...")
        else:
            print("\nAccount Not Found...")
        
    def deposit(self):

        self.depositAmount = int(input("Enter Deposit Amount: "))

        self.data[self.Acc_no]["Balance"] = int(self.data[self.Acc_no]["Balance"]) + self.depositAmount

        print("Deposit Successfully Completed....")

        with open("db/customers.json", 'w') as file:
            json.dump(self.data, file, indent=4)
           
        
    def withdraw(self):

        self.withdrawAmount = int(input("Enter Withdraw Amount: "))

        self.data[self.Acc_no]["Balance"] = int(self.data[self.Acc_no]["Balance"]) - self.withdrawAmount

        print(f"\nAmount of {self.withdrawAmount}rs Successfully Withdraw....")

        with open("db/customers.json", 'w') as file:
            json.dump(self.data, file, indent=4)
       

    def view_balance(self):

        print("\nYour Balance is:", self.data[self.Acc_no]["Balance"])

    def close_account(self):

        confirm = input("You conform Delelte your Account (yes/no)").strip().lower()

        if confirm == "yes":
            del self.data[self.Acc_no]

            with open("db/customers.json", 'w') as file:
                json.dump(self.data, file, indent=4)
            print("Delete Account successfully..")
        else:
            print("Account Not Deleted...")

    def fund_transfer(self):
        pass

    def view_statement(self):
        pass

    def update_details(self):
        pass

    def ExitToMainMenu(self):
        pass
            
c = Customer()

# c.my_account()
# c.deposit()