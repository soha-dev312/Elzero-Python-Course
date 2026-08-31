class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner   # => Public
        self._account_type = "VIP"   # => Protected
        self.__pin = pin   # => Private
    def get_pin(self):  # => Getter
        return self.__pin

acc = BankAccount("Ahmed", 5000, 1234)
print(acc.owner)
print(acc._account_type)
#print(acc.__pin) => Private
print(acc.get_pin())
        