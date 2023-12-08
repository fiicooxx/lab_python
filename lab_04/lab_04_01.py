import math

class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Incorrect values!")
        self.a = a
        self.b = b
        self.c = c
        self.name = 'Triangle'

    def surface(self):
        x = (self.a + self.b + self.c)/2
        s = math.sqrt(x*(x-self.a)*(x-self.b)*(x-self.c))
        return s

    def perimeter(self):
        p = self.a + self.b + self.c
        return p
    
    def display(self):
        print(self.name)

class Rectangle:
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Incorrect values!")
        self.a = a
        self.b = b
        self.name = "Rectangle"
        
    def surface(self):
        s = self.a * self.b
        return s
    
    def perimeter(self):
        p = 2*self.a + 2*self.b
        return p
    
    def display(self):
        print(self.name)

class Circle:
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Incorrect values!")
        self.r = r
        self.name = "Circle"

    def surface(self):
        s = math.pi * math.pow(self.r,2)
        return s
    
    def perimeter(self):
        p = 2*math.pi*self.r
        return p
    
    def display(self):
        print(self.name)

def main():
    triangle = Triangle(3,4,5)
    print(triangle.surface())
    print(triangle.perimeter())
    triangle.display()

    rectangle = Rectangle(2,4)
    print(rectangle.surface())
    print(rectangle.perimeter())
    rectangle.display()

    circle = Circle(6)
    print(circle.surface())
    print(circle.perimeter())
    circle.display()

    # Wrong credentials test
    # wrong_triangle = Triangle(10, 0, 1)
    # wrong_rectangle = Rectangle(2, -2)
    # wrong_circle = Circle(0)

main()