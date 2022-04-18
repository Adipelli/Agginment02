from BankPackage import BankInfo as BNK
class BNK:
    def __init__(self,balance,name):

        self.balance=balance
        self.name=name
    def __str__(self):
        return f"Name={self.name}\nbalance={self.balance}"
    def __eq__(self,other):
        return self.balance==other.balance

    def __noteq__(self, other):
        return self.balance != other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance
    def __gteq__(self, other):
        return self.balance >= other.balance
    def __lteq__(self, other):
        return self.balance <= other.balance
acct1 = BNK.Account(5000, "Sachin")
acct1.Deposit(1000)
acct1.Withdrawal(2000)
print(acct1)


acct2 = BNK.Account(3000, "Ali")
acct2.Deposit(500)
acct2.Withdrawal(250)
print(acct2)

if(acct1 == acct2):
    print("Thay have equal balance")
else:
    print("Thay have different balance")


if(acct1 != acct2):
    print("Oops!!! they are not equal")
else:
    print("wow!!!  they are equal")


if(acct2 > acct1):
    print("acct2 should pay more tax")
else:
    print("acct1 should pay normal tax")

if(acct2 < acct1):
    print("Sponsor for two children")
else:
    print("Start an Orphanage")

if(acct2 >= acct1):
    print("Go On Europe Trip")
else:
    print("Go for an excursion")


if(acct2 <= acct1):
    print("We can have coffee")
else:
    print("We can have meals")


acct1.AddNominee("Ranjini")
acct1.AddNominee("Ragini")
acct1.AddNominee("Malini")
acct1.AddNominee("Rukmini")


print(len(acct1))  # number of nominees


for nom in acct1:  # should iterate nominees
    print(nom)
