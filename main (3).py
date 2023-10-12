class CustomerAccount:
    def __init__(self, account_number, first_name, last_name, balance=0.0):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def get_account_info(self):
        return f"Account Number: {self.account_number}\nName: {self.first_name} {self.last_name}\nBalance: ${self.balance}"

# Create customer accounts
account1 = CustomerAccount("001", "John", "Doe", 1000.0)
account2 = CustomerAccount("002", "Jane", "Smith", 500.0)

# Perform transactions
print(account1.deposit(200))
print(account2.withdraw(100))

# Get account information
print("\nAccount 1 Information:")
print(account1.get_account_info())

print("\nAccount 2 Information:")
print(account2.get_account_info())



