"""### **Functions (10 tasks):**
1. **Basic Function**: Write a function `greet()` that takes a name as input and prints a greeting message."""
def greet():
    name="Ace"
    print("Welcome ",name)
greet()
print()

"""2. **Function with Arguments**: Create a function `area_of_rectangle()` that takes `length` and `width` as arguments and returns the area_of_rectangle."""
def area_of_rectangle(length,width):
    return length * width
l, w = 10, 20
print(f"Area of rectangle {area_of_rectangle(l, w)}")
print()

"""3. **Default Arguments**: Write a function `power(base, exponent=2)` that returns the base raised to the exponent, with a default exponent of 2."""
def power(base, exponent=2):
    return base ** exponent
print(power(10))
print()

"""4. **Return Multiple Values**: Create a function `calculate(num1, num2)` that returns the sum, difference, product, and division of two numbers."""
def calculate(num1, num2):
    return num1 + num2,num1/num2,num1*num2,num1-num2
print(calculate(10,20))
print()

"""5. **Keyword Arguments**: Write a function `introduction(name, age, country="India")` that prints a message with the provided details."""
def introduction(name, age, country="India"):
    print(f"Name : {name}\nAge : {age}\nCountry : {country}")
introduction("Ace",21)
print()

"""6. **Variable-length Arguments**: Write a function `find_max(*args)` that returns the maximum value from a variable number of arguments."""
def find_max(*args):
    count = 0
    for _ in args:
        count += 1
    return count
print(find_max("apple","orange","banana"))
print()

"""7. **Lambda Function**: Use a lambda function to filter out even numbers from a list."""
l = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, l))
print(even_numbers)

"""8. **Higher-order Function**: Write a function `apply_operation(func, a, b)` that takes another function as an argument and applies it to `a` and `b`. Test with addition, subtraction, multiplication functions.
9. **Map, Filter, Reduce**: Use `map` to square elements in a list, `filter` to get odd numbers, and `reduce` to sum all elements.
10. **Function Decorator**: Write a decorator `execution_time` that calculates and prints the time taken by a function to execute.

### **Recursion (5 tasks):**
1. **Factorial Calculation**: Write a recursive function to find the factorial of a number.
2. **Fibonacci Sequence**: Create a recursive function `fibonacci(n)` that returns the nth Fibonacci number.
3. **Sum of List Elements**: Write a recursive function to calculate the sum of elements in a list.
4. **String Reversal**: Write a recursive function that takes a string as input and returns the reversed string.
5. **Binary Search**: Implement a recursive binary search function that takes a sorted list and a target value as inputs and returns the index of the target if found, or -1 if not."""