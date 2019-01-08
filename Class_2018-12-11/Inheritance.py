from math import pi

# define what is common

class Shape:
    colour = ""


class Circle(Shape):
    radius = 0

    def __init__(self, r, c):
        self.radius = r
        self.colour = c

    def get_area(self):
        return (pi*self.radius**2)


class Rect(Shape):
    len = 0
    height = 0

    def __init__(self, l, h, c):
        self.len = l
        self.height = h
        self.colour = c

    def get_area(self):
        return (self.len*self.height)


rect = Rect(5,3, "red")

print ("My {} shape's area is {}".format(rect.colour, rect.get_area()))