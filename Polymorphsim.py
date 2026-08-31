class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")
class Square(Shape):
    def draw(self):
        print("Drawing a Square")
shapes = [Circle(), Square()]
for s in shapes:
    s.draw()