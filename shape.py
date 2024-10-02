from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
@abstractmethod
def volume(self):
        pass
class Trapezium(Shape): 
    def __init__(self, length, breath, height):
        self.length = length
        self.breath = breath
        self.height = height
def area(self):
 return 0.5 * (self.length + self.breath) * self.height
def volume(self):
 return 0.333 * ( 0.5 * (self.length + self.breath) * self.height ) * self.height
class Square(Shape):
    def __init__(self, length):
        self.length = length
def area(self):
 return self.length ** 2
def volume(self):
 return 4 * self.length
# The following line will raise an exception because Shape cannot be instantiated
# s = Shape()
# Creating Circle and Rectangle objects
t = Trapezium(3, 5, 8)
s = Square(9)
print(f"Area of the Trapezium: {t.area()}")
print(f"Volume of the Trapezium: {t.volume()}")
print(f"Area of the Square: {s.area()}")
print(f"Volume of the Square: {s.volume()}")