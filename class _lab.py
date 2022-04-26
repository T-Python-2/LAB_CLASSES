class Vehicle:
  
    #class attribute
    kingdom = "this the bird kingdom"

    #define initializer of class
    def __init__(self, brand: str, name:str , color:str , capacity:int, plate_number:int):
        #object / instance properties / attributes
        self.brand = brand 
        self.name = name 
        self.color = color 
        self.capacity = capacity 
        self.plate_number = plate_number 
    
    def set_brand(self, brand):
        if(isinstance(brand, str)):
            self.brand = brand
        else:
            raise ValueError("Value is not of type float")
    
    #define a method to get the value (read)
    def get_brand(self):
        return self.brand


    def set_name(self, name):
        if(isinstance(name, str)):
            self.name = name
        else:
            raise ValueError("Value is not of type float")
    
    #define a method to get the value (read)
    def get_name(self):
        return self.name


    def set_color(self, color):
        if(isinstance(color, str)):
            self.color = color
        else:
            raise ValueError("Value is not of type float")
    
    #define a method to get the value (read)
    def get_color(self):
        return self.color


    def set_capacity(self, capacity):
        if(isinstance(capacity, int)):
            self.capacity = capacity
        else:
            raise ValueError("Value is not of type float")
    
    #define a method to get the value (read)
    def get_capacity(self):
        return self.capacity



    def set_plate_number(self, plate_number):
        if(isinstance(plate_number, int)):
            self.plate_number = plate_number
        else:
            raise ValueError("Value is not of type float")
    
    #define a method to get the value (read)
    def get_plate_number(self):
        return self.plate_number


    def drive(self):
        print(f"the {self.name} is driving!")
    def drift(self):
        print(f"the {self.name} is drifting !!")
    def carry_cargo(self):
        print(f"the {self.name} is carrying cargo !!")

    #define a method to set a value
    def set_weight(self, weight):
        if(isinstance(weight, float)):
            self.__weight = weight
        else:
            raise ValueError("Value is not of type float")

class Bus(Vehicle):
#overriding a function / polymorphism
    def drift(self):
        print(f"the {self.name} can't drift !!")

class Truck(Vehicle):
#overriding a function / polymorphism
    def carry_cargo(self):
        print(f"the {self.name} do not carry cargo !!") 

#instantiate an object / instance
v1 = Vehicle("toyota","camry", "white", 5, 1324)
v2 = Bus("merceds","tourrider", "blue", 32, 4231)
v3 = Truck("fiat","682 n3 tractor", "yellow", 2, 3341)

v1.drive() 
v2.drift()
v3.carry_cargo()