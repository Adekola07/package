class Polygon:
    def render(self):
        print("Rendering Polygon ....")
class Square(Polygon):
    def render(self):
        print("Rendering Square ....")
class Circle(Polygon):
    def render(self):
        print("Rendering Circle ....")
s1 = Square()
c1 = Circle()

s1.render()  
c1.render()      