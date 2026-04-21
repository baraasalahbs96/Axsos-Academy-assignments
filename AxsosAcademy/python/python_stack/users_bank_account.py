class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {
            "checking": BankAccount(0.01, 0),
            "savings": BankAccount(0.02, 0)
        }

    def make_deposit(self, amount, account_type):
        self.accounts[account_type].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_type):
        self.accounts[account_type].withdraw(amount)
        return self

    def display_user_balance(self, account_type):
        print(f"{self.name} - {account_type}: {self.accounts[account_type].balance}")
        return self


user1 = User("Baraa", "baraa@mail.com")

user1.make_deposit(200, "checking").user1.make_deposit(500, "savings").user1.make_withdrawal(50, "checking").user1.display_user_balance("checking").user1.display_user_balance("savings")