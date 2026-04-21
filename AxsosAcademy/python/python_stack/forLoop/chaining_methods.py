class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bank_account = 0
     
    def make_deposite(self, amount):
        self.bank_account += amount
        self.make_deposite()
        return self
    
    def make_withdrawal(self, amount):
        self.bank_account -= amount
        self.make_withdrawal()
        return self
    
    def display_user_balance(self):
        self.bank_account()
        print(f"User: {self.name}, Balance: ${self.bank_account}")
        return self
        
        
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self
        
        
        # example  
    user1 = User("baraa", "baraa@gmail.com") 
    user1.name = "baraa" 
    user1.email = "baraa@gmail.com"
    user1.bank_account = 0
    
    user1.make_deposite(100).user1.make_deposite(200).user1.make_deposite(300).user1.make_deposite(400)
    user1.make_withdrawal(100).user1.make_withdrawal(100)
    user1.display_user_balance()
    >>   user1.make_deposite(100).user1.make_deposite(200).user1.make_deposite(300).user1.make_deposite(400)
.user1.make_withdrawal(100).user1.make_withdrawal(100).user1.display_user_balance()