class Vehicle:

    def __init__(self, brand , name ,color,capacity,plate_number):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def set_brand(self, brand):
        self.__brand = brand

    def set_name(self, name):
        self.__name = name

    def set_color(self, color):
        self.__color = color

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_plateNumber(self, plate_number):
        self.__plate_number = plate_number



    def get_brand(self):
        return self.__brand  

    def get_name(self):
        return self.__name 

    def get_color(self):
        return self.__color 

    def get_capacity(self):
        return self.__capacity

    def get_plateNumber(self):
        return self.__plate_number

      

    def drive(self):
         print(f"the {self.__name} is draving !!" )

    def drift(self):
         print(f"the {self.__name} is drifting !!" )

    def carry_cargo(self):
        print(f"the {self.__name} is carrying cargo !!" )

class Bus(Vehicle):
    def busBehavior(self):
        super().drive()
        super().drift()
        super().carry_cargo()

class Truck(Vehicle):
    def trackBehavior(self):
        super().drive()
        super().drift()
        super().carry_cargo()

v1 = Vehicle("toyota","car","red",4, 1111)
b1 = Bus("bus", "schoolBus","yellow",16,2222)
t1 = Truck("tracks", "foodTruck","blue",10, 3333)

v1.drive()
v1.drift()
v1.carry_cargo()
print("=================================")
b1.busBehavior()

print("=================================")
t1.trackBehavior()




