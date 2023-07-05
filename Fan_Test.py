from Fan_Class import FAN

fan1 = FAN(3, 1, 10, 'Yellow')
fan2 = FAN(2,0,5,'Blue')

print("\nFan number 1\n")
fan1.get_speed()
fan1.get_radius()
fan1.get_color()
fan1.get_power()
print("\nFan number 2\n")
fan2.get_speed()
fan2.get_radius()
fan2.get_color()
fan2.get_power()