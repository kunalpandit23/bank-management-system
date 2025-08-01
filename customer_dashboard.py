import json

class Customer():

    def customer_options(self):
            
            while True: 
                print("----------------------------------------------------------")          
                print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Close Account\n5. Exit")
                print("----------------------------------------------------------")

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
        
        
    def deposit(self):
        print("----------------------------------------------------------")
        self.depositAmount = int(input("Enter Deposit Amount: "))
        print("----------------------------------------------------------")

        self.data[self.Acc_no]["Balance"] = int(self.data[self.Acc_no]["Balance"]) + self.depositAmount

        print("----------------------------------------------------------")
        print(f"        {self.depositAmount}₹ is Successfully Deposit")
        print("----------------------------------------------------------")

        with open("db/customers.json", 'w') as file:
            json.dump(self.data, file, indent=4)
           
        
    def withdraw(self):
        print("----------------------------------------------------------")
        self.withdrawAmount = int(input("Enter Withdraw Amount: "))
        print("----------------------------------------------------------")
        try:
            if self.withdrawAmount > self.data[self.Acc_no]["Balance"]:
                raise Exception("Inceficient balance")
            else:
                self.data[self.Acc_no]["Balance"] = int(self.data[self.Acc_no]["Balance"]) - self.withdrawAmount
                print("----------------------------------------------------------")
                print(f"        Amount of {self.withdrawAmount}₹ is Successfully Withdraw")
                print("----------------------------------------------------------")
                with open("db/customers.json", 'w') as file:
                    json.dump(self.data, file, indent=4)

        except Exception as e:
            print("----------------------------------------------------------")
            print(e)
            print("----------------------------------------------------------")


        

    def view_balance(self):

        print("----------------------------------------------------------")
        print(f"        Account Balance: {self.data[self.Acc_no]["Balance"]}₹")
        print("----------------------------------------------------------")

    def close_account(self):
        print("----------------------------------------------------------")
        confirm = input("You conform Delelte your Account (yes/no)").strip().lower()
        print("----------------------------------------------------------")

        if confirm == "yes":
            del self.data[self.Acc_no]

            with open("db/customers.json", 'w') as file:
                json.dump(self.data, file, indent=4)
            print("----------------------------------------------------------")
            print("         Account is successfully deleted")
            print("----------------------------------------------------------")
 
        else:
            print("----------------------------------------------------------")
            print("         Account deleted process is canceled")
            print("----------------------------------------------------------")

    def fund_transfer(self):
        pass

    def view_statement(self):
        pass

    def update_details(self):
        pass

    def ExitToMainMenu(self):
        self.my_account()
            
