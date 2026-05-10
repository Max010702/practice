''' CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITANCE
    (3) POLIMORPHISM
'''

print("==== ENCAPSULATION ====")
'''
C++ JAVA > public private protected
PHP TypeScript > public private protected
Python > name __name _name
'''


class Account():
    # state
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        # self.amount = self.amount + amount
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("-----")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("-----")
# my_account.amount = 1000000
# my_account.owner = "Martin"
# my_account.amount = 1000000
# my_account.get_balance()
# print(my_account.owner)

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)

# account_owner = my_account.holder  # state
# print("account_owner:", account_owner)

print("owner before:", my_account.holder)  # state

# my_account.change_ownership("Martin")
my_account.holder = "Martin"

print("owner after:", my_account.holder)
