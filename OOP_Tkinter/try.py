from math import sqrt

class Rectangle():
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def width(self):
        return self._width
    def set_width(self, new_width):
        self._width = new_width
    
    def height(self):
        return self._height
    def set_height(self, new_height):
        self._height = new_height

    def get_area(self):
        return (self._width * self._height)
    
    def get_perimeter(self):
        return (2*(self._width + self._height))
    
    def get_diagonal(self):
        return (sqrt(self._width*self._width + self._height*self._height))
    
    def get_picture(self):
        printables = ''
        if self._height > 50 or self._width > 50:
            return "Too big for picture."
        for i in range(self._height):
            for j in range(self._width):
                printables += '*'
            printables += '\n'
        return printables
    
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

    def get_amount_inside(self, obj):
        return (self.get_area() / int(obj.get_area()))


class Square(Rectangle):
    def __init__(self, side_length):
        self._side_length = side_length

    def width(self):
        return self.width
    def set_width(self, new_width):
        self._side_length = new_width

    def height(self):
        return self.height
    def set_height(self, new_height):
        self._side_length = new_height
    
    def side_length(self):
        return self._side_length
    def set_side(self, new_side):
        self._side_length = new_side
    
    def get_picture(self):
        printable = ''
        for _ in range(self._side_length):
            for _ in range(self._side_length):
                printable += "*"
            printable += "\n"
        return printable
    
    def get_area(self):
        return (self._side_length * self._side_length)
    
    def get_perimeter(self):
        return (4*(self._side_length))
    
    def get_diagonal(self):
        return (sqrt(2 * (self._side_length)**2))

    def __str__(self):
        return f"Square(side={self._side_length})"
    
    
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())        
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))