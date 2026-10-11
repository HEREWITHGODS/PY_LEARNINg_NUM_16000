class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 1.8) + 32

    def set_celsius(self, value):
        self.celsius = value

temp1 = Temperature(15)
print(temp1.to_fahrenheit())
temp1.set_celsius(20)
print(temp1.to_fahrenheit())
#--------------------------------------
class Stack:
    def __init__(self, items: list):
        self.items = items

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

box = Stack(["toy", "phone", "headphones"])