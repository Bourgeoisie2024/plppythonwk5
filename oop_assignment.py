# OOP Assignment

# I'll create a class representing a Smartphone with attributes and methods, and add an inheritance layer to explore polymorphism and encapsulation.

# Assignment 1: Design Your Own Class! 🏗️
class Smartphone:
    """
    A class to represent a smartphone.
    """
    def __init__(self, brand, model, storage, battery_life):
        """
        Initialize the smartphone with brand, model, storage, and battery life.
        """
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def display_info(self):
        """
        Display the smartphone's information.
        """
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery_life} hours battery life."

    def charge(self):
        """
        Simulate charging the smartphone.
        """
        return f"{self.model} is charging."

class Smartwatch(Smartphone):
    """
    A class to represent a smartwatch, inheriting from Smartphone.
    """
    def __init__(self, brand, model, storage, battery_life, strap_material):
        """
        Initialize the smartwatch with brand, model, storage, battery life, and strap material.
        """
        super().__init__(brand, model, storage, battery_life)
        self.strap_material = strap_material

    def display_info(self):
        """
        Display the smartwatch's information.
        """
        return f"{self.brand} {self.model} with {self.storage}GB storage, {self.battery_life} hours battery life, and {self.strap_material} strap."

    def charge(self):
        """
        Simulate charging the smartwatch.
        """
        return f"{self.model} smartwatch is charging."

# Creating instances
phone = Smartphone("Apple", "iPhone 13", 128, 20)
watch = Smartwatch("Apple", "Apple Watch Series 7", 32, 18, "Silicone")

# Displaying information
print(phone.display_info())
print(watch.display_info())

# Charging devices
print(phone.charge())
print(watch.charge())

# Activity 2: Polymorphism Challenge! 🎭
# I'll create a program with different vehicles, each having a move() method that behaves differently.

class Vehicle:
    """
    A base class to represent a vehicle.
    """
    def move(self):
        """
        A method to be overridden by subclasses to define movement.
        """
        pass

class Car(Vehicle):
    """
    A class to represent a car, inheriting from Vehicle.
    """
    def move(self):
        """
        Simulate the car's movement.
        """
        return "Driving 🚗"

class Plane(Vehicle):
    """
    A class to represent a plane, inheriting from Vehicle.
    """
    def move(self):
        """
        Simulate the plane's movement.
        """
        return "Flying ✈️"

class Boat(Vehicle):
    """
    A class to represent a boat, inheriting from Vehicle.
    """
    def move(self):
        """
        Simulate the boat's movement.
        """
        return "Sailing 🚤"

# Creating instances
car = Car()
plane = Plane()
boat = Boat()

# Displaying movement
print(car.move())
print(plane.move())
print(boat.move())
