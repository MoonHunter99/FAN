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
    def set_speed(self):
        self.__speed = int(input("PLease input the number(1,2,3) to set your desired speed: "))
    def get_power(self):
        if self.__power == False:
            print("The Fan is off")
        elif self.__power == True:
            print("The Fan is on")
    