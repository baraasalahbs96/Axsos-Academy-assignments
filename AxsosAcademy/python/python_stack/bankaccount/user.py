class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bank_account = 0
     
    def make_deposite(self, amount):
        self.bank_account += amount
        self.make_deposite()
        
    def make_withdrawal(self, amount):
        self.bank_account -= amount
        self.make_withdrawal()
        
    def display_user_balance(self):
        self.bank_account()
        print(f"User: {self.name}, Balance: ${self.bank_account}")
        return self
        self.display_user_balance() 
        
        
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self
        self.display_user_balance()