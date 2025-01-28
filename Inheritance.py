### **Easy Level**
"""1. **Single Inheritance:**
   Create a base class `Person` with attributes `name` and `age`. Derive a class `Student` that adds an attribute `student_id` and a method `display_student_info()`."""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self,name,age,student_id):
        #super().__init__(name,age) #super() function that will make the child class inherit all the methods and properties from its parent
        Person.__init__(self,name,age)
        self.student_id = student_id
    def display_student_info(self):
        print(f"Name : {self.name}, Age : {self.age} and Student ID : {self.student_id}")
person = Student("Ace",22,201161003)
person.display_student_info()
print()

"""2. **Multilevel Inheritance:**
   Create a base class `Animal` with a method `sound()`. Derive a class `Mammal` that adds `has_hair` as an attribute. Further derive a class `Dog` that implements the `sound()` method to return "Bark"."""
class Animal:
    @staticmethod
    def sound():
        print("Dog sound : Hahaha")
class Mammal(Animal):
    def __init__(self, has_hair, breed):
        self.has_hair = has_hair
        self.breed = breed
class Dog(Mammal):
    def __init__(self, has_hair, breed):
        super().__init__(has_hair,breed)
    def sound(self):
        print("Dog sound : Kukuku")
obj = Dog(True, "Labrador")
obj.sound()
print(f"Breed : {obj.breed} and Dog has hair : {obj.has_hair}")
print()


"""3. **Multiple Inheritance:**
   Create two base classes:
   - `Engine` with a method `start_engine()`.
   - `Wheels` with a method `rotate_wheels()`.
   Derive a class `Car` that uses both methods."""
class Engine:
    @staticmethod
    def start_engine():
        return "Start"
class Wheels:
    @staticmethod
    def rotate_wheels():
        return "Rotate wheels"
class Car(Engine,Wheels):
    def drive(self):
        engine = super().start_engine()
        wheel = super().rotate_wheels()
        return f"Car Engine : \"{engine}\" and Wheel : \"{wheel}\""
obj = Car()
print(obj.drive())
print()

"""4. **Method Overriding:**
   Create a base class `Shape` with a method `area()` returning `"Not defined"`. Override the method in a derived class `Rectangle` to calculate and return the area."""
class Shape:
    def area(self):
        return "Not defined"
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

rectangle = Rectangle(5, 3)
print(rectangle.area())
print()

"""5. **Super Function:**
   Create a base class `Vehicle` with an `__init__()` method to initialize `brand`. In the derived class `Car`, use `super()` to call the `Vehicle` constructor while adding an additional attribute `model`."""
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model

obj = Car("Tata","SUV")
print(f"Car : \"{obj.brand}\" and Model : \"{obj.model}\"")
print()

### **Intermediate Level**
"""6. **Single Inheritance with Method Overriding:**
   Create a base class `Employee` with a method `salary()` returning a fixed value. Override the method in a derived class `Manager` to return a higher salary."""
class Employee:
    @staticmethod
    def salary():
        return 30000
class Manager(Employee):
    def salary(self):
        return 50000

obj1 = Employee()
obj2 = Manager()
print(f"Before Employee salary : \"{obj1.salary()}\" and After Manager salary : \"{obj2.salary()}\"")
print()


"""7. **Multilevel Inheritance with Super:**
   Create classes `A`, `B`, and `C` (where `B` is derived from `A` and `C` is derived from `B`). Implement a method `show()` in each class and call the parent class's `show()` method using `super()`."""
class A:
    @staticmethod
    def show():
        print("Class A")
class B(A):
    def show(self):
        super().show()
        print("Class B")
class C(B):
    def show(self):
        super().show()
        print("Class C")

obj = C()
obj.show()
print()

""""8. **Multiple Inheritance with Conflicting Methods:**
   Create two base classes, both having a method `greet()`. Derive a class that resolves the conflict using the Method Resolution Order (MRO)."""
class A:
    @staticmethod
    def greet():
        return "Hello from A"
class B:
    @staticmethod
    def greet():
        return "Hello from B"
class C(A,B):
    def greet(self):
        return super().greet()

obj = C()
print(obj.greet())
print()

"""9. **Method Chaining:**
   Create a base class `Calculator` with methods `add()` and `subtract()`. Chain these methods in a derived class `AdvancedCalculator` to perform multiple operations."""
class Calculator:
    def add(self):
        return 5 + 10,self
    @staticmethod
    def sub():
        return 10 - 5
class AdCal(Calculator):
    def res(self):
        return super().add(),super().sub()

obj = AdCal()
print(obj.add(),obj.sub())
print()


"""10. **Super Function in Multiple Inheritance:**
    Create two base classes `X` and `Y` with methods `show()` and `display()`. Use `super()` in a derived class to resolve the order of method calls."""
class X:
    def show(self):
        print("X show")
class Y:
    @staticmethod
    def display():
        print("Y display")
class Z(X,Y):
    def show(self):
        super().show()
        super().display()
        print("Class Z")

z = Z()
z.show()
print()

### **Advanced Level**
"""11. **Custom Initialization in Multilevel Inheritance:**
    Create classes `Person`, `Employee`, and `Manager` (multilevel inheritance). Each class should initialize additional attributes and call the parent class's constructor using `super()`."""
class Person:
    def __init__(self,name):
        self.name = name
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id = emp_id
class Manager(Employee):
    def __init__(self,name,emp_id,salary):
        super().__init__(name,emp_id)
        self.salary = salary
    def show(self):
        print(f"Name : {self.name}, Employee ID : {self.emp_id} and Salary : {self.salary}")

obj = Manager("Ace",201161003,50000)
obj.show()
print()


"""12. **Dynamic Method Overriding:**"
    Create a base class `Transport` with a method `travel_time()`. Override the method dynamically in derived classes `Bus` and `Train` based on given distance and speed."""
class Transport:
    def travel_time(self,distance,speed):
        return distance / speed
class Bus(Transport):
    def travel_time(self, distance, speed):
        return super().travel_time(distance, speed) * 1.5

class Train(Transport):
    def travel_time(self, distance, speed):
        return super().travel_time(distance, speed) * 1.2

bus = Bus()
train = Train()

print(bus.travel_time(100, 50))
print(train.travel_time(100, 50))
print()


"""13. **Decorator with Single Inheritance:**
    Use a decorator method in a derived class to extend the functionality of a base class method."""


"""14. **Multiple Inheritance with Super and MRO:**
    Demonstrate a complex MRO scenario where three classes share a common base class, and `super()` ensures the correct order of execution."""
class A:
    @staticmethod
    def show():
        print("Class A")
        return "Class A"

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    def show(self):
        super().show()

d = D()
d.show()  # Output: Class B
print()


"""15. **Custom Exception in Inheritance:**
    Create a base class `MathOperation` with a method `divide()` and a derived class that raises a custom exception when dividing by zero."""
class MathOperation:
    @staticmethod
    def divide(x,y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y
operation = MathOperation()
try:
    print(operation.divide(10, 0))
except ZeroDivisionError as e:
    print(e)
print()


"""16. **Polymorphism with Method Overriding:**
    Create a base class `Appliance` with a method `power_consumption()`. Override it in derived classes `Fridge` and `Microwave` with specific calculations."""
class Appliance:
    def power_consumption(self):
        return "Generic consumption"

class Fridge(Appliance):
    def power_consumption(self):
        return "200W"

class Microwave(Appliance):
    def power_consumption(self):
        return "800W"

fridge = Fridge()
microwave = Microwave()

print(fridge.power_consumption())  # Output: 200W
print(microwave.power_consumption())  # Output: 800W
print()


"""17. **Multilevel Inheritance with Method Chaining:**
    Implement multilevel inheritance where each class modifies a common method `update()` and calls the next class in the chain."""
class A:
    @staticmethod
    def update():
        return "Updated in A"

class B(A):
    def update(self):
        return super().update() + " and B"

class C(B):
    def update(self):
        return super().update() + " and C"

c = C()
print(c.update())
print()


"""18. **Multiple Inheritance with Interfaces:**
    Implement a scenario where two base classes act as interfaces, and the derived class combines their functionality."""
class Interface1:
    @staticmethod
    def method1():
        return "Method 1"

class Interface2:
    @staticmethod
    def method2():
        return "Method 2"

class ConcreteClass(Interface1, Interface2):
    def combined(self):
        return self.method1() + " and " + self.method2()

obj = ConcreteClass()
print(obj.combined())  # Output: Method 1 and Method 2
print()

"""19. **Hybrid Inheritance:**
    Demonstrate hybrid inheritance by combining single, multilevel, and multiple inheritance in a single example."""
class A:
    @staticmethod
    def show():
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    @staticmethod
    def display():
        print("Class C")

class D(B, C):
    def display_all(self):
        super().show()
        super().display()

d = D()
d.display_all()
print()


"""20. **Advanced Method Overriding with Super:**
    Create a hierarchy where multiple derived classes override a base class method and call the base implementation using `super()`."""
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Mammal(Animal):
    def sound(self):
        parent_sound = super().sound()  # Call the base class method
        return f"{parent_sound}, but it is warm-blooded"

class Dog(Mammal):
    def sound(self):
        parent_sound = super().sound()  # Call the parent class (Mammal) method
        return f"{parent_sound}, and it barks"

class Puppy(Dog):
    def sound(self):
        parent_sound = super().sound()  # Call the parent class (Dog) method
        return f"{parent_sound}, and it yips like a puppy"

# Create an instance of the Puppy class
puppy = Puppy()

# Call the sound() method
print(puppy.sound())
print()

#Method Chain
class A:
    def show(self):
        print("Class A")
        return self
class B(A):
    @staticmethod
    def dis():
        print("Class B")
obj = B()
print(obj.show().dis())