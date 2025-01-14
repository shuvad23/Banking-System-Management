# Account Opening class---------------------------------------
class customerAccountManagementOpening:
    LastName=None
    Firstname=None
    DateOfBirth=None
    NationalID=None
    EmailAddress=None
    _password=None
    saveDate=[]
    accountbalance=0

    def __init__(self):
        pass
    def accountOpening(self,last,first,date,id,email,Pass):
        self.LastName=last
        self.Firstname=first
        self.DateOfBirth=date
        self.NationalID=id
        self.EmailAddress=email
        self._password=Pass
    def saveAccount(self):
        savedate={
            "LastName":self.LastName,
            "FirstName":self.Firstname,
            "Date Of Birth":self.DateOfBirth,
            "National ID":self.NationalID,
            "Email Address":self.EmailAddress,
            "Password":self._password,
            "Account Balance":self.accountbalance
                  }
        self.saveDate.append(savedate)
    
    def accountHistory(self):
        with open("AccountHistory.csv",'w') as filename:
            for data in self.saveDate:
                filename.write(f"{data['LastName']},{data['FirstName']},{data['Date Of Birth']},{data['National ID']},{data['Email Address']},{data['Password']},{data['Account Balance']}\n")

# Deposit class-----------------------------------
class basicTransactionsDeposit(customerAccountManagementOpening):
    def __init__(self,email,Pass):
        deposit=int(input("Plz Enter Your Deposit Amount: "))
        for data in self.saveDate:
            if (email== data['Email Address']) and (Pass== data['Password']):
                data['Account Balance']+=deposit
                print("\n")
                print("Deposit Successfully!.........")
                print("----------------------------------------------------------")
                break

# Viewing Balance class----------------------------------------------------------
class customerAccountManagementViewing(customerAccountManagementOpening):

    def __init__(self,email,Pass):
        for data in self.saveDate:
            if (email in data['Email Address']) and (Pass in data['Password']):
                print("\n")
                print("Account Name: ",data['FirstName'],data['LastName'])
                print("Your Current Balance is : ",data['Account Balance'],"Tk")
                print("-----------------------------------------------------------------------")
                break

# Withdrawal class
class basicTransactionsWithdrawal(customerAccountManagementOpening):

    def __init__(self,email,Pass):
        withdrawal=int(input("Plz Enter Your Withdrawal Amount: "))
        for data in self.saveDate:
            if (email== data['Email Address']) and (Pass== data['Password']):
                data['Account Balance']-=withdrawal
                print("\n")
                print("Withdrawal Successfully!.........")
                print("----------------------------------------------------------")
                break
                 
            

while True:
    print("\n\t\tXYZ BANK LIMITED"
          "\n"
          "\n\tCustomer Account Management: "
          "\n\t1. Opening Account"
          "\n\t2. Viewing Balance"
          "\n\tBasic Transactions: "
          "\n\t3. Deposit"
          "\n\t4. Withdrawal"
          "\n\t0. Exit"
          #"\n\t5. Transaction History Viewing"
          #"\n\t6. Basic reporting"
          #"\n\t7. User Authentication"
          )
    option=int(input("Enter the Option: "))
    if(option==0):
        print("Thanks for using our service!.............Have a nice day.....")
        break
    match option:
        case 1:
            account1=customerAccountManagementOpening()
            account1.LastName=input("Enter the Last Name: ")
            account1.Firstname=input("Enter the First Name: ")
            account1.DateOfBirth=input("Enter the Date OF Birth: ")
            account1.NationalID=input("Enter the National ID: ")
            account1.EmailAddress=input("Enter the Email Address: ")
            account1._password=input("Enter the Password: ")
            account1.accountOpening(account1.LastName,account1.Firstname,account1.DateOfBirth,account1.NationalID,account1.EmailAddress,account1._password)
            account1.saveAccount()
            account1.accountHistory()
            print("\tAccount Opening Successfully!....")
            print("-------------------------------------------------------------------")
            
        case 2:
            email=input("Enter the Email Address: ")
            password=input("Enter the Password: ")
            customerAccountManagementViewing(email,password)
        case 3:
            email=input("Enter the Email Address: ")
            password=input("Enter the Password: ")
            basicTransactionsDeposit(email,password)
        case 4:
            email=input("Enter the Email Address: ")
            password=input("Enter the Password: ")
            basicTransactionsWithdrawal(email,password)
        