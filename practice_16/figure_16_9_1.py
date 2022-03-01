class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Triangle sides: a = {self.a}, b = {self.b}, c = {self.c}'

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Rectangle sides: x = {self.x}, y = {self.y}'

trianle_1 = Triangle(2,3,4)
rect_1 = Rectangle(5,10)

print(str(trianle_1))
print(str(rect_1))