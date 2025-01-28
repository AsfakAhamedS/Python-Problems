### **Function-Based Tasks**

"""1. **Basic Class and Object Creation:**
   - Create a class `Person` with properties `name` and `age`. Instantiate an object and print its properties."""
class Person: #Class
    def __init__(self,name,age): #Instance Variable
        self.name = name
        self.age = age

p1 = Person("Ace",22) #Object for Class
print(f"Name : {p1.name} and Age : {p1.age}")
print()

"""2. **Using the `__init__()` Method:**
   - Create a class `Book` with properties `title` and `author` using the `__init__()` method. Instantiate two objects with different data."""
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

b1 = Book("Vampire Chronicles","Anne Rice")
b2 = Book("Harry Potter","J.K. Rowling")
print(f"Title : {b1.title} and Author : {b1.author} \nTitle : {b2.title} and Author : {b2.author}")
print()

"""3. **Implementing `__str__()` Method:**
   - Define a `Car` class. Add `brand` and `model` properties. Use `__str__()` to return a string representation of the car details."""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Car Brand : {self.brand} and Model : {self.model}"

c1 = Car("Rolls Royce","Ghost")
print(c1)
print()


"""4. **Object Method:**
   - Create a `Calculator` class with methods for addition, subtraction, multiplication, and division."""
class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        print(f"Addition = {self.x + self.y}")
    def sub(self):
        print(f"Subtraction = {self.x - self.y}")
    def mul(self):
        print(f"Multiplication = {self.x * self.y}")
    def div(self):
        if self.y != 0:
            print(f"Divisible = {self.x / self.y}")
        else:
            print("Your value not divisible")

obj = Calculator(10,0)
a,s,m,d = obj.add(),obj.sub(),obj.mul(),obj.div()
print()

"""5. **Modify Object Properties:**
   - Define a class `Student` with properties `name` and `marks`. Create a method `update_marks` to modify the `marks` property of an object."""
class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    """def update_marks(self, new_marks): #Another method to0 update values
         self.marks = new_marks"""
    def __str__(self):
        return f"Name = {self.name} and Mark = {self.mark}"

s1 = Student("Ace",50)
print("Before :",s1)
#student.update_marks(90)
s1.mark = 90
print("After :",s1)
print()


"""6. **Delete Object Properties:**
   - Implement a class `Employee` with properties `name` and `department`. Add a method to delete the `department` property of an object."""
class Emp:
    def __init__(self,name,dep):
        self.name = name
        self.dep = dep
    """def delete_department(self): #Another method to delete
        del self.department"""
    def __str__(self):
        return f"Name : {self.name} and Department : {self.dep}"

e1 = Emp("Ace","Developer")
print("Before",e1)
#employee.delete_department()
del e1.dep
print("After Name :",e1.name)
print()

"""7. **Delete Objects:**
   - Create a class `Animal`. Write a function that creates an instance of the class and deletes it after printing its properties."""
class Animal:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Name : {self.name}"

a1 = Animal("Ace")
print("Before",a1)
del a1
print("After delete Animal class object a1, get error")
print()

"""8. **Object Count:**
   - Create a `Counter` class with a class variable to count the number of instances created."""
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

obj1 = Counter()
obj2 = Counter()
print(f"Number of objects created: {Counter.count}")
print()


"""9. **Dynamic Property Addition:**
   - Implement a class `DynamicObject`after the object is  where you can add new properties dynamically a created."""
class DynamicObject:
    pass

obj = DynamicObject()
obj.new_property = "Dynamic Value"
obj.new_property = "Dynamic Value"
print(obj.new_property,obj.new_property)
print()

"""10. **Inheritance and `__str__`:**
    - Create a base class `Shape` with a `color` property. Create a derived class `Circle` with an additional property `radius`. Use `__str__()` to display details of a `Circle` object."""
class Shape:
    @staticmethod
    def color():
        colors = "Red"
        return colors

class Circle(Shape):
    def __init__(self,radius):
        self.color = super().color()
        self.radius = radius
    def __str__(self):
        return f"Color : {self.color} and Radius : {self.radius}"
obj = Circle(5)
print(obj)
print()


### **Recursion-Based Tasks**

"""11. **Recursive Factorial with Class:**
    - Create a `Math` class with a method `factorial` that calculates the factorial of a number recursively."""
class Math:
    def factorial(self,n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)
obj = Math()
print("Factorial ",obj.factorial(5))
print()


"""12. **Recursive Sum of Digits:**
    - Define a class `Number` with a method `sum_of_digits` that uses recursion to find the sum of digits of an integer."""
class Number:
    def sum_of_digits(self,n):
        if n == 0:
            return 0
        return n % 10 + self.sum_of_digits(n//10)
        # res = 0
        # while n > 0:
        #     rem = n % 10
        #     res = res + rem
        #     n = n // 10
        # return res
obj = Number()
print("Sum of Digit = ",obj.sum_of_digits(2024))
print()


"""13. **Recursive Fibonacci:**
    - Create a `Series` class with a method `fibonacci` that returns the nth Fibonacci number using recursion."""
class Series:
    def fibonacci(self,n):
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

obj = Series()
print(f"Fibonacci Series : {obj.fibonacci(10)}")
print()


"""14. **Recursive Palindrome Check:**
    - Write a `StringProcessor` class with a method `is_palindrome` that checks if a string is a palindrome using recursion."""
class StringPro:
    def is_palindrome(self,n):
        if len(n) <= 1:
            return True
        # if n.lower()[0:] == n.lower()[::-1]:
        #     return True
        # else:
        #     return False
        if n.lower()[0] != n.lower()[-1]:
            return False
        return self.is_palindrome(n[1:-1])
""" Logic
Input: "madam"
is_palindrome("madam")

Compare 'm' (first) and 'm' (last): Equal
Call is_palindrome("ada")
is_palindrome("ada")

Compare 'a' (first) and 'a' (last): Equal
Call is_palindrome("d")
is_palindrome("d")

Length is 1 (base case): Return True
"""

obj = StringPro()
ch = obj.is_palindrome("Aca")
print(f"Palindrome : {ch}")
print()

"""15. **Recursive Power Calculation:**
    - Implement a class `Exponent` with a method `power` to compute \( a^b \) using recursion."""
class Exponent:
    def power(self, base, expon):
        if expon == 0:
            return 1
        return base * self.power(base, expon - 1)

exp = Exponent()
print(exp.power(2, 3))

"""### **16. Basic Usage of Class Variables** (Easy)  
Create a `Student` class with a class variable `school_name` set to `"Green Valley High School"`. Create three `Student` objects and print the `school_name` for each object.  """
class Student:
    school_name = "Green Valley High School"

obj_stu1 = Student()
obj_stu2 = Student()
obj_stu3 = Student()
obj_stu2.school_name = "Red Valley High School"
obj_stu3.school_name = "Blue Valley High School"
print(obj_stu1.school_name,obj_stu2.school_name,obj_stu3.school_name)
print()


### **2. Modifying Class Variables** (Easy-Intermediate)
"""Create a `Car` class with a class variable `wheels` set to `4`. Write a method that allows you to change the value of the class variable. Instantiate two car objects, change the number of wheels to `6` using one object, and show that it reflects in both objects.  """
class Car:
    wheel = 4

    @classmethod
    def change_wheel(cls,new_wheel):
        cls.wheel = new_wheel
car1 = Car()
car2 = Car()
print("Before ",car1.wheel)
car1.change_wheel(6)
print("After ",car2.wheel)
print()


### **3. Tracking Object Count** (Intermediate)  
"""Create a `Book` class with a class variable `book_count`. Increment this variable in the constructor (`__init__`) every time a new object is created. Add a method to display the total number of books created. Test the class by creating 5 `Book` objects and displaying the total count."""
class Book:
    book_count = 0
    def __init__(self):
        Book.book_count += 1
    @classmethod
    def display_count(cls):
        print(f"Total books: {cls.book_count}")
book1 = Book()
book2 = Book()
Book.display_count()
print()


### **4. Shared and Instance-Specific Data** (Intermediate-Advanced)  
"""Create a `Department` class with a class variable `company_name` set to `"TechCorp"`. Add an instance variable `department_name` for each object. Demonstrate how the class variable is shared among all instances but the instance variable is unique for each.  """
class Department:
    company_name = "TechCrop"
    def __init__(self, department_name):
        self.department_name = department_name  # Instance variable

dept1 = Department("HR")
dept2 = Department("Engineering")
dept3 = Department("Sales")

print(dept1.company_name, dept1.department_name)
print(dept2.company_name, dept2.department_name)
print(dept3.company_name, dept3.department_name)
print()


### **5. Using Class Variables for Configuration** (Advanced)  
"""Create a `Website` class with class variables `domain` and `protocol` (default: `"example.com"` and `"https"`). Add a method `get_url()` that constructs and returns the full URL using the class variables. Update the `domain` and `protocol` for a specific use case (e.g., switching to `"http"` for testing) and demonstrate the effect.  """
class Website:
    domain = "example.com"  # Class variable
    protocol = "https"  # Class variable

    @classmethod
    def update_configuration(cls, new_domain, new_protocol):
        cls.domain = new_domain
        cls.protocol = new_protocol

    @classmethod
    def get_url(cls):
        return f"{cls.protocol}://{cls.domain}"

# Default configuration
print(Website.get_url())  # Output: https://example.com

# Update configuration
Website.update_configuration("testsite.com", "http")
print(Website.get_url())  # Output: http://testsite.com


