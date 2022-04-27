'''
## define a Vehicle class . it has the following structure :
#### properties
- brand
- name
- color
- capacity
- plate_number
#### methods
- drive()
  prints "the vehicle_name is driving!"
- drift()
  prints "the vehicle_name is drifting !!" or something else depending on the class.
- carry_cargo()
  prints "the vehicle_name is carrying cargo !!" or something else depending on the class
### for each of the properties do a setter & getter (encabsulate the data).
### Create tow other subclasses (inherit from vehicle):
- Bus
- Truck
### Note
- override  the methods as needed for each subclass of vehicle. 
- create at least one object of each class.
- call all the methods on each object.
'''
from turtle import color


class Vehicle:
    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:int):
        self.__brand=brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number
        
        
             

    def set_brand(self,brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_color(self,color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_capacity(self,capacity):
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity
    def set_plate_number(self,plate_number):
        self.__plate_number = plate_number

    def get_plate_number(self):
        return self.__plate_number
    
    def drive(self):
        print(f"the {self.__name} driving")    
    def drift(self):
        print(f"the {self.__name} is drifting")
    def carry_cargo(self):
        print(f"the {self.__name} is carrying cargo !!") 
    
class Bus(Vehicle):

    def drift(self):
        print(f"drift the {self.set_name} if you can.")

    def carry_cargo(self):
        super().carry_cargo()
        print(f"the {self.set_name} bus is big enough")

class Truck(Vehicle):
    def drift(self):
        print(f"drift the {self.set_name} truck if you have a death wish.")

    def carry_cargo(self):
        print(f"the {self.set_name} Truck is all you need")
    
car1=Vehicle("Honda","Accird","White",5,905)
bus1=Bus("Toyota","mini bus","Black",25,990)
truck1=Truck("Mercedes","Actros L","green",2,121)   

#Vehicle.drive()
#Vehicle.drift()
#Vehicle.carry_cargo()
print("_____________________________________")
bus1.drift()
bus1.carry_cargo()
print("_____________________________________")
truck1.drift()
truck1.carry_cargo()
 