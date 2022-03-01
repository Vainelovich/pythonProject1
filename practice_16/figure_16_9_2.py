class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def rect_area(self):
        return self.a * self.b

newRect = Rectangle(11, 22)
print(newRect.rect_area())