#-----------------------------------------------
class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages
    def info(self):
        return "Book {self.title}, {self.pages}"

book1 = Book("Master and Margarite", 555)
print(book1.info())
book2 = Book("WAR AND PEACE", 909)
print(book2.info())
#-----------------------------------------------
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

rectangles = [
    Rectangle(100, 200),
    Rectangle(200, 300),
    Rectangle(300, 400),
]

squares = [s.area() for s in rectangles]
print(squares)
#-----------------------------------------------
class RangeGenerator:
    def __init__(self, start, step):
        self.start = start
        self.step = step

    def generate(self, n):
        for i in range(n):
            yield self.start + i * self.step

generator1 = RangeGenerator(100, 10)
generator2 = RangeGenerator(24, 3)
generator3 = RangeGenerator(0, 1)
for i in generator1.generate(5):
    print(i)
print("-"*5)
for i in generator2.generate(5):
    print(i)
print("-"*5)
for i in generator3.generate(5):
    print(i)
print("-"*5)