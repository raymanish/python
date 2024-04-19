class Account:
    count = 100000

    def __init__(self, newType):
        # Increment account count and assign account number
        Account.count += 1000
        self.AccNum = Account.count
        self.AccType = newType
        self.AccBal = 0.00

    def getNum(self):
        # Get account number
        return self.AccNum

    def getType(self):
        # Get account type
        return self.AccType

    def setType(self):
        # Set account type
        print(f"Current Account Type: {self.AccType}")
        print("SAVINGS", "CHEQUE", "BUSINESS")
        newType = input("Enter New Account TYPE: ")
        self.AccType = newType

    def getBal(self):
        # Get account balance
        return self.AccBal

# Function for use: This class represents a bank account and provides methods to get and set account details such as number, type, and balance.
