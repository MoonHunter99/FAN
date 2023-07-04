class FAN:
    def __init__(self, speed = 1, power = 0, radius = 5, color = 'Blue'):
        self.__speed = speed
        self.__power = power
        self.__radius = radius
        self.__color = color
    def get_speed(self):
        if self.__speed == 1:
            print("SLOW")
        elif self.__speed == 2:
            print("MEDIUM")
        elif self.__speed == 3:
            print("FAST")
    def set_speed(self):
        self.__speed = int(input("Please input the number(1,2,3) to set your desired speed: "))
    def get_power(self):
        if self.__power == 0:
            print("The Fan is off")
        elif self.__power == 1:
            print("The Fan is on")
    def set_power(self):
        self.__power = int(input("Please input the number(0/1) to set the power state of the Fan: "))
        if self.__power == 0:
            print("The Fan is set as: Off")
        elif self.__power == 1:
            print("The Fan is set as: On")
    def get_radius(self):
        print("The radius is", self.__radius)
    def set_radius(self):
        self.__radius = float(input("Please input the number to set the radius of the Fan: "))
        print("The Radius is now set to",self.__radius)
    def get_color(self):
        print("The Fan color is", self.__color)
    def set_color(self):
        self.__color = str(input("Please input what color you want to set the fan to be: "))
    