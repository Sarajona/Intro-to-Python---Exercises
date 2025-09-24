from datetime import datetime

class Car:
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
    

my_car = Car("Toyota Previa", 1995)
my_car.desription()
my_car.age()

your_car = Car("Lexus 1A", 1975)
your_car.desription()
your_car.age()
