from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
@abstractmethod
def perimeter(self):
    pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
def area(self):
 return 3.14 * self.radius ** 2
def perimeter(self):
 return 2 * 3.14 * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
def area(self):
 return self.width * self.height
def perimeter(self):
 return 2 * (self.width + self.height)
# The following line will raise an exception because Shape cannot be instantiated
# s = Shape()
# Creating Circle and Rectangle objects
c = Circle(5)
r = Rectangle(4, 6)
print(f"Area of the circle: {c.area()}")
print(f"Perimeter of the circle: {c.perimeter()}")
print(f"Area of the rectangle: {r.area()}")
print(f"Perimeter of the rectangle: {r.perimeter()}")