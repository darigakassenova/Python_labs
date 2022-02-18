class Account():
    balance=0
    owner="idiot"
    def _init_(self):
        self.cash=int(input())
    def deposit(self,balance):
        balance+=self.cash
    def withdraw(self,balance):
        withdr=int(input())
        if balance>=withdr:
            print(withdr)
        else:
            print("You don't have enough money!, get the hell out of here , you fool!")

a = Account()
a._init_()
a.deposit()
a.withdraw()
