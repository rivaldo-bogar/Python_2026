class BankAccount():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance 
    def deposit(self,amount):
        self.balance += amount
       
        # untuk penambahan saldo
    def withdraw(self,wid):
        #Mengurangi saldo
        self.balance = self.balance - wid
        pass
    def show_balance(self):
        # Menampilkan saldo
        print(f"sisa saldo A.n : {self.owner}\n saldo = {self.balance}")
        pass

account1 = BankAccount('valdo',2000)
account2 = BankAccount('bogar',7000)
account1.deposit(2000)
account1.withdraw(1000)
account1.show_balance()
account2.deposit(2000)
account2.withdraw(1000)
account2.show_balance()