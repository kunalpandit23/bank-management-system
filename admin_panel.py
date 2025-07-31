import json
class Admin:
    def __init__(self):

        # self._Id = "Admin"
        # self.__password = "@Admin.23"
        self.AdminInfo = {}

    # @property
    # def password(self):
    #     return self.__password
    
    # @password.setter
    # def password(self, forgot_password):
    #     self.__password += forgot_password


    def Admin_login(self):
        print("\n1. Login with ID & Password\n2. forgot ID & Password")
        user_input = input()
        try:
                with open("db/admin.json", 'r') as file:
                    self.AdminInfo = json.load(file)

        except FileNotFoundError:
                self.AdminInfo = {}

        if user_input == "login" or user_input == "1":
            id = input("\nEnter your Admin ID: ")
            password = input("\nEnter your Password: ")

            if id == self.AdminInfo["Admin1"]["ID"] and password == self.AdminInfo["Admin1"]["Password"]:
                print("\nAdmin login successfully...")

                print("\n1. View Account\n2. Search Account\n3. Delete Account\n4. Exit")
                another_input = input()

                if another_input == "viewaccount" or another_input == "1":
                    a.ViewAllAccount()                   
                elif another_input == "searchaccount" or "2":
                    a.SearchAccount()
                elif another_input == "deleteaccount" or "3":
                    a.DeleteAccount()
                else:
                    
                    print("\nINVALID INPUT...")

            else:
                print("\nInvalid ID, Password.")

        elif user_input == "forgotpasswort" or "forgot" or user_input == "2":


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
                print("Wrong answer")
            
           

            with open("db/admin.json", 'w') as file:
                json.dump(self.AdminInfo, file, indent=4)

        else:
            print("INVALID INPUT")
          
        

    
    def ViewAllAccount(self):
        print("\nview accoount successfully...")
        pass

    def SearchAccount(self):
        print("\nsearch account successfully...")
        pass

    def DeleteAccount(self):
        print("\ndelete account successfully...")
        pass
    
    def ViewAllTransaction(self):
        pass

    def TotalBankBalance(self):
        pass
    
    def ExitToMainMenu(self):
        pass
a = Admin()

# a.Admin_login()