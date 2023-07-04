class FAN:
    def __init__(self, speed = 1, power = False, radius = 5, color = 'Blue'):
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