from math import pi

class Shape:
    colour = ""

    def __init__(self, colour):
        self.__colour = colour

    def get_colour(self):
        return self.__colour


class Circle(Shape):

    def __init__(self, radius, colour):
        self.__radius = radius
        super().__init__(colour)

    def get_radius(self):
        return self.__radius

    def get_area(self):
        return(pi*self.__radius*self.__radius)

    def get_perimeter(self):
        return(2*pi*self.__radius)


class Rectangle(Shape):

    def __init__(self, width, length, colour):
        self.__width = width
        self.__length = length
        super().__init__(colour)

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def get_area(self):
        return(self.__width*self.__length)

    def get_perimeter(self):
        return(2*(self.__width+self.__length))


class Square(Shape):

    def __init__(self, length, colour):
        self.__length = length
        super().__init__(colour)

    def get_length(self):
        return self.__length

    def get_area(self):
        return(self.__length*self.__length)

    def get_perimeter(self):
        return(2*(self.__length+self.__length))


class ShapeCollection:

    def __init__(self):
        self.__shape_collection = []

    def add_circle(self, circle: Circle):
        self.__shape_collection.append(circle)

    def add_square(self, square: Square):
        self.__shape_collection.append(square)

    def add_rectangle(self, rectangle: Rectangle):
        self.__shape_collection.append(rectangle)

    def get_collection_list(self):
        return self.__shape_collection

    def clear_collection_list(self):
        self.__shape_collection = []


    def get_total_area(self):
        total_area = 0
        for shape in self.__shape_collection:
            total_area += shape.get_area()
        return total_area

    def get_total_perimeter(self):
        total_perimeter = 0
        for shape in self.__shape_collection:
            total_perimeter += shape.get_perimeter()
        return total_perimeter


    def get_shape_count(self):
        return len(self.__shape_collection)


circle1 = Circle(10, "Blue")

print("Circle colour is", circle1.get_colour())
print("Circle area is", round(circle1.get_area(), 2))
print("Circle perimeter is", round(circle1.get_perimeter(), 2))


rectangle1 = Rectangle(5, 6, "Red")

print("Rectangle colour is", rectangle1.get_colour())
print("Rectangle area is", round(rectangle1.get_area(), 2))
print("Rectangle perimeter is", round(rectangle1.get_perimeter(), 2))


square1 = Square(50, "Yellow")

print("Square colour is", square1.get_colour())
print("Square area is", round(square1.get_area(), 2))
print("Square perimeter is", round(square1.get_perimeter(), 2))


collection1 = ShapeCollection()
collection1.add_circle(Circle(15, "White"))
collection1.add_square(Square(12, "Brown"))
collection1.add_rectangle(Rectangle(13, 12, "Pink"))


print("COLLECTION total area", round(collection1.get_total_area(),2))
print("COLLECTION total perimeter", round(collection1.get_total_perimeter(),2))
print("COLLECTION size", collection1.get_shape_count())
print("COLLECTION ", collection1.get_collection_list())

