class BankAccount:

    accounts = []

    def __init__(self, account_rate = 0.01, account_balance = 0):
        self.account_rate = account_rate
        self.account_balance = account_balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        print(f"This account now has ${self.account_balance}")
        return self

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
            print(f"This account now has ${self.account_balance} after withdrawal")
        else:
            self.account_balance = self.account_balance - 5
            print("Insufficient Funds, charging a $5 NSF fee")
        return self

    def display_account_info(self):
        print(f"Funds: ${self.account_balance}\nAPY: {(1+ self.account_rate)}%")
        return self

    def yield_interest(self, rate):
        self.account_balance = self.account_balance + (1+ rate)
        print(f"This account now has ${self.account_balance} after {rate} accrual")
        return self

    @classmethod
    def display_bank_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

checking = BankAccount(0.05, 150)
savings = BankAccount(0.02, 1000)

checking.deposit(500)

checking.display_account_info()

checking.withdraw(200)

checking.yield_interest(0.06)

savings.deposit(200)

savings.yield_interest(0.02)

savings.withdraw(300) #conditional check

savings.display_account_info()

BankAccount.display_bank_accounts()