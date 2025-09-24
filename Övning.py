from datetime import datetime


#KLASSER OCH OBJEKT
class car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.current_year = datetime.now().year

    def desription(self):
        print("My car:")
        print("brand = ", self.brand)
        print("year = ", self.year)
    def age(self):
        print(self.current_year - self.year)
    

my_car = car("Toyota Previa", 1995)
my_car.desription()
my_car.age()

your_car = car("Lexus 1A", 1975)
your_car.desription()
your_car.age()

print("\n-------------------\n")

# Arv och polymorfism #
class Vehicle:
    def __init__(self, brand):    
        self.brand = brand
    def drive(self):
        print("I'm a vehicle and I'm driving!")

class Car(Vehicle):
    def drive(self):
        print("Vroom vroom I'm a car and I am driving")

class Bicycle(Vehicle):
    def drive(self):
        print("Pling pling I'm a bicycle and I am cycling")

class Boat(Vehicle):
    def drive(self):
        print("Hooonk Hooonk I'm a boat and I'm floating")
       
bicycle_one = Bicycle("Monark")
car_one = Car("Tesla")
boat_one = Boat("Candela")

bicycle_one.drive()
car_one.drive()
boat_one.drive()
print("\n------------------\n")
list_of_vehicles = [Car("Tesla"), Bicycle("Monark"), Boat("Candela")]
for v in list_of_vehicles:
    v.drive()

print("\n------------------\n")
