# Assignment 1: Design Your Own Class

# Base class representing a generic Appliance
class Appliance:
    def __init__(self, brand, power, warranty):
        self.brand = brand
        self.power = power  # in watts
        self.warranty = warranty  # in years
    
    def turn_on(self):
        return f"{self.brand} appliance is now ON. Consuming {self.power}W of power."
    
    def turn_off(self):
        return f"{self.brand} appliance is now OFF."
    
    def get_warranty_info(self):
        return f"This {self.brand} appliance comes with a {self.warranty}-year warranty."

# Derived class representing a specific type of appliance: Washing Machine
class WashingMachine(Appliance):
    def __init__(self, brand, power, capacity, warranty, mode):
        super().__init__(brand, power, warranty)
        self.capacity = capacity  # in kg
        self.mode = mode  # Washing mode
    
    def wash_clothes(self):
        return f"Washing clothes in {self.brand} washing machine ({self.capacity}kg) using {self.mode} mode."

# Creating an object of WashingMachine
wm = WashingMachine("Samsung", 2000, 7, 2, "Eco Wash")
print(wm.turn_on())
print(wm.wash_clothes())
print(wm.get_warranty_info())
print(wm.turn_off())


# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass  # Abstract method

class Car(Vehicle):
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type
    
    def move(self):
        return f"{self.brand} car is Driving 🚗 using {self.fuel_type}."

class Plane(Vehicle):
    def __init__(self, airline, speed):
        self.airline = airline
        self.speed = speed  # in km/h
    
    def move(self):
        return f"{self.airline} plane is Flying ✈ at {self.speed} km/h."

class Boat(Vehicle):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity  # in passengers
    
    def move(self):
        return f"{self.name} is Sailing ⛵ with {self.capacity} passengers aboard."

# Demonstrating polymorphism
vehicles = [Car("Tesla", "Electric"), Plane("Emirates", 900), Boat("Titanic", 3000)]
for v in vehicles:
    print(v.move())
