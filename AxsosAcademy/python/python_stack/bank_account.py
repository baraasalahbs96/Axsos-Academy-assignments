class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = 0.01
        self.balance = 0
    def deposit(self, amount):
      self.balance += amount
      return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a 5$ fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
        
    def display_account_info(self):
            print(f"Balance: {self.balance}$")
            return self
        
    def yield_interest(self):
            if self.balance > 0:
                self.balance += self.balance * self.int_rate
            return self

# Account 1:
account1 = BankAccount(int_rate=0.05, balance=0)
account1.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()

# Account 2: 
account2 = BankAccount(int_rate=0.03, balance=0)
account2.deposit(500).deposit(300).withdraw(100).withdraw(50).withdraw(75).withdraw(25).yield_interest().display_account_info()
