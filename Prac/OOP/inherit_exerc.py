class Parent:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        print(f"Привет, я {self.name}")

class Child(Parent):          # ← указываем родителя
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name)     # вызываем __init__ родителя
        self.age = age

    def greet(self) -> None:       # переопределяем метод
        print(f"Привет, я {self.name}, мне {self.age} лет")

MAMA = Parent("MAMA")
SON = Child("SON", 18)
MAMA.greet()
SON.greet()
#--------------------------------------------------------------
class Vehicle:
    def __init__(self, brand: str) -> None:
        self.brand = brand
    def start(self):
        return self.brand + " lunch!!"
class Car(Vehicle):
    def __init__(self, brand: str, model: str) -> None:
        super().__init__(brand)
        self.model = model
    def start(self):
        return f"Car {self.brand} {self.model} lunch"
class ElectricCar(Car):
    def __init__(self, brand: str, model: str, battery: int):
        super().__init__(brand, model)
        self.battery = battery

    def start(self):
        return f"{super().start()}. Battery: {self.battery} mAh"


car = Vehicle("BMW")
print(car.start())
tachka = Car("Audi","R8")
print(tachka.start())
electric_car = ElectricCar("Tesla","Plade",3500)
print(electric_car.start())
