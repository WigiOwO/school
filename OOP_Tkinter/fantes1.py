class Fan:
    SLOW   = 1
    MEDIUM = 2
    FAST   = 3

    def __init__(self, speed=1, radius=5, color="blue", on=False):
        self.__speed  = speed
        self.__radius = radius
        self.__color  = color
        self.__on     = on

    def get_speed(self):   return self.__speed
    def get_radius(self):  return self.__radius
    def get_color(self):   return self.__color
    def is_on(self):       return self.__on

    def set_speed(self, speed):   self.__speed  = speed
    def set_radius(self, radius): self.__radius = radius
    def set_color(self, color):   self.__color  = color
    def set_on(self, on):         self.__on     = on

    def __str__(self):
        return f"Speed: {self.__speed}\nRadius: {self.__radius}\nColor: {self.__color}\nStatus: {self.__on}"