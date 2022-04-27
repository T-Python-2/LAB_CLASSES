#1 define a Vehicle class . and build the structure :
from os import name
import re


class Vehicle:
    def __init__(self, brand: str, name: str, color: str, capacity: float, plate_number:int):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

  # define setters 
    def set_brand(self , brand):
        if (isinstance(brand , str)):
            self.__brand = brand
        else:
            raise ValueError("Incorrect brand name !!")


    def set_name(self, name):
         if (isinstance(name, str)):
            self.__name = name
         else:
            raise ValueError("Incorrect name !!")


    def set_color(self, color):
         if (isinstance(color, str)):
            self.__color = color
         else:
            raise ValueError("Incorrect color name !!")


    def set_capacity(self, capacity):
        if (isinstance(capacity, float)):
            self.__capacity = capacity
        else:
            raise ValueError("Incorrect Value !!")
        

    def set_plate_number(self, plate_number):
        if (isinstance(plate_number, int)):
            self.__plate_number = plate_number
        else:
            raise ValueError("Incorrect Value !!")



  # define getters 
    def get_brand(self):
        return self.__brand

    def get_name(self):
        return self.__name
    
    def get_color(self):
        return self.__color
    
    def get_brand(self):
        return self.__capacity

    def get_brand(self):
        return self.__plate_number



   # Methods 
    def drive(self):
         return print(f"the {self.__name}is driving!")


    def drift(self):
        return print(f"the {self.__name} is drifting !!")


    def carry_cargo(self):
        return print(f"the {self.__name} is carrying cargo !!")

#####################



# Subclasses 
class Bus(Vehicle):

    def drive(self):
        return super().drive()

    def drift(self):
        return print(f"The Bus{name} didn't drift ")

    def carry_cargo(self):
        return print("The Bus doesn't carrying cargo ! ")

    

##################

class Truck(Vehicle):

    def drive(self):
        return super().drive()

    def drift(self):
        return print("The Truck is Warming ")

    def carry_cargo(self):
         print(f"The {name} in its way! ")


     ############



# Create the objects 

car = Vehicle("Audi" , "a8" , "black" , 15.2 , 1998)
car.drive()
car.drift()
car.carry_cargo()

bus = Bus("MAN" , "solaris" , "white" , 26.4 , 4413)
bus.drive()
bus.drift()
bus.carry_cargo()

truck = Truck("Volvo" , "Volvo FH" , "orange" , 40.2 , 2819)
truck.drive()
truck.drift()
truck.carry_cargo()

    



    




        



