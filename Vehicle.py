class Vehicale:
    def __init__(self, brand: str, name:str, color:str, capacity:int, plate_number:int):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self. __capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
        print("the {} is driving!".format(self.__name))

    def drift(self):
        print("the {} is drifting !!".format(self.__name))
    
    def carry_cargo(self):
        print("the {} is carrying cargo !!".format(self.__name))


    def set_brand(self, brand):
       self.__weight = brand
    
    def set_name(self, name):
       self.__name = name
    
    def set_color(self, color):
       self.__color = color
    
    def set_capacity(self, capacity):
        if(isinstance(capacity, int)):
            self.__capacity = capacity
        else:
            raise ValueError("Value is not of type integer")
    
    def set_plateNumber(self, plate_number):
        if(isinstance(plate_number, int)):
            self.__plate_number = plate_number
        else:
            raise ValueError("Value is not of type integer")
    

    #define a method to get the value (read)
    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand
    
    def get_color(self):
        return self.__color
    
    def get_capacity(self):
        return self.__capacity

    def get_plateNumber(self):
        return self.__plate_number


class Bus(Vehicale):
    
    def drift(self):
        super().drift()
        print(" and type vehicle is bus")

class Truck(Vehicale):
    def drift(self):
        super().drift()
        print(" and type vehicle is truck")


car1 = Vehicale("eee", "car1", "red", 4, 1234)
car1.drive()
car1.drift()
car1.carry_cargo()

car2 = Bus("eee", "car2", "white", 50, 1534)
car2.drive()
car2.drift()
car2.carry_cargo()

car3 = Truck("eee", "car3", "black", 2, 1454)
car3.drive()
car3.drift()
car3.carry_cargo()