### **Easy Tasks**
"""1. **Abstract Class Basics**
   - Create an abstract class `Animal` with an abstract method `make_sound()`.
   - Implement two subclasses: `Dog` and `Cat`, where each provides its version of `make_sound()`."""
import math
from abc import ABC,abstractmethod #Import Abstract methods

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"
obj = Dog()
obj1 = Cat()
print(f"Dog sound : {obj.make_sound()} and Cat sound : {obj1.make_sound()}")
print()


"""2. **Checking Abstract Class Restrictions**  
   - Try to create an object of an abstract class directly and observe the error. Document your findings."""
class Abs(ABC):
    @abstractmethod
    def sound(self):
        pass

try:
    obj = Abs()
    print(obj.sound())
except Exception as e:
    print(f"Error occured : \"{e}\"")
print()

"""3. **Abstract Method with Parameters**  
   - Create an abstract class `Shape` with an abstract method `area()`.  
   - Implement two subclasses, `Rectangle` and `Circle`. Calculate the area based on given parameters."""
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    # def set_dimensions(self, width, height):
    #     self.width = width
    #     self.height = height
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def area(self):
        return self.width * self.height
class Circle(Shape):
    # def set_dimensions(self, radius):
    #     self.radius = radius
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

rectangle = Rectangle(5,10)
circle = Circle(7)

#Without using Constructor
# # Set dimensions for the shapes
# rectangle.set_dimensions(5, 10)
# circle.set_dimensions(7)

print(f"Rectangle : {rectangle.area()} and Circle : {circle.area()}")
print()



### **Intermediate Tasks**  
"""4. **Multiple Methods in an Abstract Class**
   - Create an abstract class `Appliance` with methods `turn_on()` and `turn_off()`.  
   - Create subclasses `Fan` and `Light` that implement these methods."""
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class Fan(Appliance):
    def turn_on(self):
        return "Turn on the Fan"
    def turn_off(self):
        return "Turn off the Fan"
class Ligth(Appliance):
    def turn_on(self):
        return "Turn on the Light"
    def turn_off(self):
        return "Turn off the Light"

fan = Fan()
light = Ligth()
print(f"Fan : {fan.turn_on()} and Light : {light.turn_off()}")
print()

"""5. **Abstract Class with Constructor**  
   - Create an abstract class `Vehicle` with a constructor to initialize attributes like `name` and `speed`.  
   - Create a subclass `Car` that overrides a method to display the vehicle's details."""
class Vehicle(ABC):
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    @abstractmethod
    def details(self):
        pass
class Car(Vehicle):
    def details(self):
        return f"Car Name: {self.name}, Speed: {self.speed} km/h"

car = Car("Tesla", 200)
print(car.details())
print()


"""6. **Passing Object as Argument**
   - Create a function `process_vehicle(vehicle)` that accepts an object of type `Vehicle`.  
   - Based on the passed object, call its methods and display its details."""
def process_vehicle(vehicles):
    print(vehicles.details())

vehicle = Car("BMW", 180)
process_vehicle(vehicle)
print()



### **Advanced Tasks**  
"""7. **Abstract Class and Factory Method**
   - Design an abstract class `Document` with a method `read()`.  
   - Create subclasses `PDF` and `Word`. ritWe a factory function to create objects based on the document type."""
class Document(ABC):
    @abstractmethod
    def read(self):
        pass
class Pdf(Document):
    def read(self):
        return "Read a PDF document"
class Word(Document):
    def read(self):
        return "Read a word document"
class Not(Document):
    def read(self):
        return "This document not available"

def function_factory(doc_type):
    if doc_type == "pdf":
        return Pdf()
    elif doc_type == "word":
        return Word()
    else:
        return Not()

doc = function_factory("words")
print(doc.read())
print()



"""8. **Chained Abstract Classes**  
   - Create an abstract class `Employee` with methods `calculate_salary()` and `generate_report()`.  
   - Create two intermediate abstract subclasses, `Engineer` and `Manager`.  
   - Create concrete classes `SoftwareEngineer` and `ProjectManager` that provide implementation."""
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def generate_report(self):
        pass
class Engineer(Employee,ABC):
    pass
class Manager(Employee,ABC):
    pass
class SoftwareEngineer(Engineer):
    def calculate_salary(self):
        return "Calculating Software Engineer Salary"
    def generate_report(self):
        return "Generating Software Engineer Report"

class ProjectManager(Manager):
    def calculate_salary(self):
        return "Calculating Project Manager Salary"
    def generate_report(self):
            return "Generating Project Manager Report"

se = SoftwareEngineer()
pm = ProjectManager()
print(se.calculate_salary())
print(pm.generate_report())
print()



"""9. **Abstract Method Returning Objects**  
   - Create an abstract class `Builder` with an abstract method `build_part()`.  
   - Implement a subclass `CarBuilder` that returns a `Car` object with custom properties."""
class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color
    def __str__(self):
         return f"Car Model 1 : {self.model} and Car Color : {self.color}"
    def dis(self):
        print(f"Car Model 2 : {self.model} and Car Color : {self.color}")
class Builder(ABC):
    @abstractmethod
    def build_part(self):
        pass
class CarBuilder(Builder):
    def build_part(self):
        return Car("Tesla","Red")

build = CarBuilder()
car = build.build_part()
print(car)
car.dis()
print()



"""10. **Dynamic Behavior with Abstract Class and Objects**
    - Create an abstract class `PaymentProcessor` with a method `process_payment()`.  
    - Implement `CreditCardPayment` and `UPIPayment` classes.  
    - Write a function that takes a list of payment objects and dynamically calls `process_payment()` for each."""
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self):
        return "Processing Credit Card Payment"

class UPIPayment(PaymentProcessor):
    def process_payment(self):
        return "Processing UPI Payment"

def process_payments(payment_list):
    for payment in payment_list:
        print(payment.process_payment())

payments = [CreditCardPayment(), UPIPayment()]
process_payments(payments)
print()

class Account:
    def __init__(self, owner, balance):
        self.owner = owner      # Public attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance  # Public method to access private data

# Creating an object
acc = Account("John", 1000)

# Accessing public attribute
print(acc.owner)  # John

# Accessing private attribute directly will cause an error
print(acc._Account__balance)  # AttributeError

# Using a public method to access private data
print(acc.get_balance())  # 1000

# Performing deposit and withdrawal
acc.deposit(500)
print(acc.get_balance())  # 1500
print()





