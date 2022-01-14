class bank_account:
    def __init__(self, initBal = 0, intRate = .02) -> None:
        self.account_balance = initBal
        self.interest_rate = intRate
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print(f'Current account balance: ${self.account_balance}')
        print(f'Current interest rate: {self.interest_rate * 100}%')
        return self
    def yield_interest(self):
        self.account_balance = self.account_balance + (self.account_balance * self.interest_rate)
        return self

#create 2 accounts
account1 = bank_account(800)
account2 = bank_account(6520, .05)

#first account - 3 deposits, 1 withdrawal, yield interest, then display account info (chained)
print('Account 1:')
account1.deposit(206).deposit(68).deposit(133).withdraw(350).yield_interest().display_account_info()
#second account - 2 deposits, 4 widthrawals, yield interest, then display account info (chained)
print('Account 2:')
account2.deposit(2003).deposit(76).withdraw(640).withdraw(43).withdraw(1500).withdraw(23).yield_interest().display_account_info()

#ninja bonus: use a class method to print all instances of a bank accounts info (used inside account info method)