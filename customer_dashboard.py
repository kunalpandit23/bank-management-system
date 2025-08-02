import json
from json.decoder import JSONDecodeError

class Customer():
      
    def deposit(self):

        print("----------------------------------------------------------")
        self.depositAmount = int(input("Enter Deposit Amount: "))
        print("----------------------------------------------------------")

        try:
            if self.depositAmount <= 0:
                raise Exception("Only positive Amount added")
            else:
                self.data[self.Acc_no]["Balance"] = int(self.data[self.Acc_no]["Balance"]) + self.depositAmount
                print("----------------------------------------------------------")
                print(f"        {self.depositAmount}₹ is Successfully Deposit")
                print("----------------------------------------------------------")

                with open("db/customers.json", 'w') as file:
                    json.dump(self.data, file, indent=4) 
        except Exception as e:
            print("----------------------------------------------------------")
            print(f"        {e}")
            print("----------------------------------------------------------")         
        
    def withdraw(self):
        print("----------------------------------------------------------")
        self.withdrawAmount = int(input("Enter Withdraw Amount: "))
        print("----------------------------------------------------------")
        try:
            if self.withdrawAmount > self.data[self.Acc_no]["Balance"]:
                raise Exception("Inceficient balance")
            
            if self.withdrawAmount < 0:
                raise ValueError("Negative value are not withdraw")
            
            else:
                self.data[self.Acc_no]["Balance"] = int(self.data[self.Acc_no]["Balance"]) - self.withdrawAmount
                print("----------------------------------------------------------")
                print(f"        Amount of {self.withdrawAmount}₹ is Successfully Withdraw")
                print("----------------------------------------------------------")
                with open("db/customers.json", 'w') as file:
                    json.dump(self.data, file, indent=4)

        except Exception as e:
            print("----------------------------------------------------------")
            print(f"        {e}")
            print("----------------------------------------------------------")

        except ValueError as e:
            print("----------------------------------------------------------")
            print(f"        {e}")
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
        try:
            with open("db/customers.json", 'r') as file:
                self.data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            self.data = {}

        print("----------------------------------------------------------")
        receiver_acc = input("Enter Receiver Account Number: ").strip()

        try:
            amount = int(input("Enter Amount to Transfer: "))
        except ValueError:
            print("----------------------------------------------------------")
            print("         Invalid amount entered.")
            print("----------------------------------------------------------")
            return

        print("----------------------------------------------------------")

        try:
            sender = self.data.get(self.Acc_no)
            receiver = self.data.get(receiver_acc)

            if not sender:
                raise Exception("Your account not found.")
            if not receiver:
                raise Exception("Receiver account not found.")
            if amount < 0:
                raise ValueError("Negative amounts cannot be transferred.")
            if int(sender["Balance"]) < amount:
                raise Exception("Insufficient balance.")

            # Perform transaction
            sender["Balance"] = int(sender["Balance"]) - amount
            receiver["Balance"] = int(receiver["Balance"]) + amount

            print("----------------------------------------------------------")
            print(f"        ₹{amount} successfully transferred to {receiver_acc}")
            print("----------------------------------------------------------")

            # Save updated data
            with open("db/customers.json", 'w') as file:
                json.dump(self.data, file, indent=4)

        except Exception as e:
            print("----------------------------------------------------------")
            print(f"        Error: {e}")
            print("----------------------------------------------------------")

        except ValueError as ve:
            print("----------------------------------------------------------")
            print(f"        Error: {ve}")
            print("----------------------------------------------------------")


    def view_statement(self):
        pass

    def update_details(self):
        pass

    def ExitToMainMenu(self):
        pass
            
class CustomerMenu(Customer):

    def customer_options(self):            
        while True: 
            print("----------------------------------------------------------")          
            print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Fund Transfer\n5. Close Account\n6. Exit")
            print("----------------------------------------------------------")

            another_input = input().strip().lower()      

            if another_input in ["deposit", "1"]:
                self.deposit()
            elif another_input in ["withdraw", "2"]:
                self.withdraw()
            elif another_input in ["check balance","checkbalance", "3"]:
                self.view_balance()
            elif another_input in ["fund transfer", "fundtransfer", "4"]:
                self.fund_transfer()
            elif another_input in ["close account", "checkaccount", "5"]:
                self.close_account()
                break
            elif another_input in ["exit", "6"]:
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

