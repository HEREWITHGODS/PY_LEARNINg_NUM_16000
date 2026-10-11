class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age
Sanya = Person('Sanya', 22)
print(Sanya.get_age())
#---------------------------------------------
class Wallet:
    def __init__(self, balance: int):
        self.__balance = balance

    def deposit(self, amount: int):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
wlt = Wallet(100)
wlt.deposit(150)
print(wlt.get_balance())
#----------------------------------------------
class Logger:
    def __init__(self, msg: list):
        self._msg = msg
    def log(self, msg: str):
        self._msg.append(msg)
    def get_msg(self):
        return self._msg
message = Logger(["Hello"])
print(message.get_msg())
message.log("Dolbaeb")
print(message.get_msg())


