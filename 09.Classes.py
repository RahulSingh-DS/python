# Classes
# (OOP) Object Oriented Programming is one of the most effective approaches to writing software. In object - oriented programming, you write classes that represents real - world things and situations and you create objects based on these classes. When you write a class, you define the general behavior that a whole category of objects can have.

# When you create individual objects from the class, each object is automatically equipped with the general behavior, you can then give each object whatever unique traits you desire. You will be amazed how well real -world situations can be modeled with object - oriented programming.

# Making an object from a class is called instantiations, and you work with instances of a class.

# Creating and Using a Class

class Cat:
    def __init__(self, name,age):
        # Initialize name and age attributes.
        self.name = name
        self.age = age
    def sit(self):
        # Simulate a cat sitting in response to a command.
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        # Simulate rolling over in response to a command.
        print(f"{self.name} rolled over!")
        pass
my_cat = Cat('ABC',7)
print(f"My cat's name is {my_cat.name}.")
print(f"My cat is {my_cat.age} years old.")

# The __int__() Method
# A function that's part of a class is a method. The __init__() method is a special method that python runs automatically whenever we create a new instance. This method has two leading underscores and two trailing underscores,a convention that helps prevent Python's Default method names from conflicting with your method names. Make sure to use two underscores on each side of __init__().When we use just one on each side, the method wont be called automatically when you use your class, which can result in errors that are difficult to identify.

# Making an Instance from a class

class Cat:
    def __init__(self, name,age):
        # Initialize name and age attributes.
        self.name = name
        self.age = age
    def sit(self):
        # Simulate a cat sitting in response to a command.
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        # Simulate rolling over in response to a command.
        print(f"{self.name} rolled over!")
        pass
# This is my instance from here.
my_cat = Cat('ABC',7)

# Calling Methods these are calling methods.
my_cat.sit()
my_cat.roll_over()
# Accesing Attributes
print(f"My cat's name is {my_cat.name}.") # my_cat.name is the attribute
print(f"My cat is {my_cat.age} years old.")

# Creating Multiple Instances

class Cat:
    def __init__(self, name,age):
        # Initialize name and age attributes.
        self.name = name
        self.age = age
    def sit(self):
        # Simulate a cat sitting in response to a command.
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        # Simulate rolling over in response to a command.
        print(f"{self.name} rolled over!")
        pass
my_cat = Cat('ABC',7)
your_cat= Cat('Lucy',4)

print(f"My cat's name is {my_cat.name}.")
print(f"My cat is {my_cat.age} years old.")
my_cat.sit()
print(f"\nYour cat's name is {your_cat.name}")
print(f"Your cat is {your_cat.age} years old.")
your_cat.sit()


# Working with classes and instances

# You can use classes to represent many real-world situations. once you write a class, you'll spend most of your time working with instances created from that class. yOu can modify the attributes of an instance directly or write methods that update attributes in specific ways.

#  The car class

class Car:
    # A simple attempt to represent a car.
    def __init__(self,make,model,year):
        # INtialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name.
        
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())


# Setting a Default Valu for an Attribute

class Car:
    # A simple attempt to represent a car.
    def __init__(self,make,model,year):
        # INtialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name.
        
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    # Modifying An Attribute's Value Through a Method.
    def update_odometer(self,mileage):
        # Set the odometer reading to the given value. Reject the change if it attempts to roll the odometer back.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    # Incrementing an Attribute's Value through a method.
    def increment_odometer(self,miles):
        # Add the given amount to the odometer reading.
        self.odometer_reading += miles
        
    def read_odometer(self):
        # Print a statement showing the car's mileage.
        print(f"This car has {self.odometer_reading} miles on it.")
class Battery:
    """A simple attempt to model a battery for an electric Car."""
    def __init__(self,battery_size=40):
        self.battery_size = battery_size
        
    def describe_battery(self):
        # Print a statement describing the battery size.
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        # Print a statement about the range this battery provides.
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
        
        
# The __init__() MEthod for a child class.
class ElectricCar(Car):
    # Represnts aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        # INitialize attributes of the parent class.
        # Then initialize attributes specific to an electric car.
# Defining Attributes and Methods for the child class.
        super().__init__(make,model,year)
        # self.battery_size = 40
        self.battery = Battery()
        
    def describe_battery(self):
        # Print a statement describing the battery size.
        print(f"This car has a {self.battery_size}-kWh battery.")
# Overriding methods from the Parent class.
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank")

        
my_punch = ElectricCar('tata','punch',2023)
print(my_punch.get_descriptive_name())
my_punch.battery.describe_battery()
my_punch.battery.get_range()


    
my_new_car = Car('audi','a4',2024)
my_used_car = Car('hyundai','i20',2019)
print(my_used_car.get_descriptive_name())

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23_500) #updated vALue
my_new_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# NOTE: You can use methods like this to control how users of program update values such as an odometer reading but anyone with access to the program can set the odometer reading to any value by accessing the attribute directly. Effective security takes exteme attention to detail in addition to basic checks.

# INHERITANCE
# You dont always have to start from scratch when writing a class. if the class you are writing is a specialized version of another class you wrote, you can use inheritance. when one class inherits from another, it takes on the attributes and methods of the first class.The Original class is called the parent class and the new class is the Child class. The child class can inherit any or all of the attributes and methods of its parent class, but it's also free to define new attributes and methods of its own.

# The __init__() MEthod for a child class.

# when you are writing a new class based on an existing class, you will often want to call the __init__() method from the parent class. This will intialize any attributes that were defined in the parent __init__() method and make them available in the child class.

# Overriding Methods from the parent class
# You can override any method from the parent class that doesnt fit what you are trying to model with the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.

# Instances as Attributes
# When modeling something from the real world in code, you may find that you are adding more and more details to a class. You can break your large class into smaller classes that work together, this approach is called composition.
