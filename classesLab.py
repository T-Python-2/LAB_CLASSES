
class Vehicle:

    def __init__(self, brand:str , name:str , color:str , capacity:int, plate_number:str):

        self.__brand = brand
        self.__name = name 
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
            print(f"The vehicle {self.__name}is driving!")
        
    def drift(self):
            print(f"The vehicle {self.__name} is drifiting!")
        
    def carry_cargo(self):
            print(f"The vehicle {self.__name} is carrying!" )        
        
    def set_brand(self,brand):
            self.__brand = brand
    def get_brand(self,brand):
            return self.__brand    
    
    def set_name(self,name):
            self.__name= name  
    def get_name(self,name):
            return self.__name      

    def set_color(self,color):
            self.__color= color    
    def get_color(self,color):
            return self.__color    

    def set_capacity(self,capacity):
            self.__capacity= capacity    
    def get_capacity(self,capacity):
            return self.__capacity    

    def set_plate_number(self,plate_number):
            self.__plate_number= plate_number    
    def get_plate_number(self,plate_number):
            return self.__plate_number        
        
  

        
        

class Bus(Vehicle):

    def drift(slef):
        print("You can't drifiting with a bus")
    
class Truck(Vehicle):


    def drift(slef):
        print("You can't drifiting with a truck")

    def carry_cargo(self):
        #super().carry_cargo()
        print("You can carry any type of cargo with truck")

   


vehicle1 = Vehicle("Audi","A4","White",50,"ESA123")
vehicle1.drive()
vehicle1.drift()
vehicle1.carry_cargo()
print("---------------")


bus1 = Bus("Toyota","Bus","Black",500,"BAE1234")
bus1.drive()
bus1.drift()
bus1.carry_cargo()
print("---------------")

truck1 = Truck("Ford","Truck","Red",300,"QWER123")
truck1.drive()
truck1.drift()
truck1.carry_cargo()
print("---------------")


        

        