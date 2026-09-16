class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, number_of_doors, type_of_roof):

        super().__init__("car")

        self.year = year
        self.make = make
        self.model = model
        self.number_of_doors = number_of_doors
        self.type_of_roof = type_of_roof

year = input("Please enter the year of the vehicle: ")
make = input("Please enter the make of the vehicle: ")
model = input("Please enter the model of the vehicle: ")
number_of_doors = input("Please enter the number of doors on the vehicle: ")
type_of_roof = input("Does the vehicle have a sun roof or is it solid: ")

my_vehicle = Automobile(year, make, model, number_of_doors, type_of_roof)

print("Vehicle type:", my_vehicle.vehicle_type)
print("Year:", my_vehicle.year)
print("Make:", my_vehicle.make)
print("Model:", my_vehicle.model)
print("Number of doors:", my_vehicle.number_of_doors)
print("Type of roof:", my_vehicle.type_of_roof)