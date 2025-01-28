### **Easy Level:**

"""1. Write a Python program that checks if a number is positive or negative."""
n = 20
if n > 0:
    print(f"Positive no. = {n}")
else:
    print(f"Negative no. = {n}")
print()

"""2. Create a program that checks if a number is even or odd."""
n = 31
if n % 2 == 0:
    print(f"Even no. = {n}")
else:
    print(f"Odd no. = {n}")
print()

"""3. Write a Python program to check if a person is eligible to vote (age ≥ 18)."""
person_Age = 19
if person_Age > 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
print()

"""4. Using shorthand, check if a number is greater than 10 and print "Yes" or "No"."""
n = 100
print("Yes") if n > 10 else print("No")
print()

"""5. Create a program that checks if a number is divisible by both 3 and 5."""
n = 30
if n % 3 == 0 and n % 5 == 0:
    print(f"{n} divisible for 3 and 5")
else:
    print(f"{n} not divisible for 3 and 5")
print()

"""6. Write a Python program to check the largest of two numbers."""
n1, n2 = 10, 20
if n1 > n2:
    print(f"n1 = {n1} is largest no.")
elif n1 == n2:
    print(f"n1 = {n1} and n2 = {n2} both are equal")
else:
    print(f"n2 = {n2} is largest no.")
print()

"""7. Using shorthand, write a program to check if a number is less than 100 and print "Small" or "Large"."""
n = 99
print("Small") if n < 100 else print("Large")
print()

"""8. Write a program that asks the user for a grade and prints "Pass" if the grade is 50 or more."""
user_mark = 51
print("Pass") if user_mark > 50 else print("Fail")
print()

"""9. Check if a number is between 10 and 20 using an if-else block."""
n = 11
if 10 < n < 20:
    print("Number is between 10 and 20")
else:
    print("Number in between 10 and 20")
print()

"""10. Write a Python program to check if a string is empty or not."""
empty_str = ""
if empty_str in "":
    print("String is empty")
else:
    print("Not empty")
print()

### **Intermediate Level:**

"""11. Write a program to check if a year is a leap year or not."""
leap_Year = 2028
if leap_Year % 400 == 0 or (leap_Year % 4 == 0 and leap_Year % 100 != 0):
    print(f"{leap_Year} is leap year")
else:
    print(f"{leap_Year} is not a leap year")
print()

"""12. Create a program that checks if a character is a vowel or consonant."""
char = 'C'
if char in "aeiouAEIOU":
    print(f"{char} is a vowel")
else:
    print(f"{char} is not a vowel")
print()

"""13. Write a program that asks for a score and prints "Excellent" if it's 90+, "Good" if 70-89, "Pass" if 50-69, or "Fail"."""
score = 40
print(f"{score} is Excellent") if score >= 90 else print(f"{score} is Good") if 70 <= score < 89 else print(f"{score} is Pass") if 50 <= score < 69 else print(f"{score} is Fail")
print()

"""14. Using multiple `elif` statements, write a program to determine the size of a number (e.g., Small if <10, Medium if 10-100, Large if >100)."""
num = 67
if num > 100:
    print(f"{num} is large")
elif 10 <= num <= 100:
    print(f"{num} is medium")
elif num < 10:
    print(f"{num} is small")
else:
    print(f"{num} is negative")
print()

"""15. Create a program that checks the type of a triangle (equilateral, isosceles, or scalene) based on user inputs for sides."""
"""a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")"""

"""16. Write a program that checks if a given string contains the letter "a"."""
name = "Ace"
if 'a' in name.lower():
    print("The string contains 'a'")
else:
    print("The string does not contain 'a'")
print()

"""17. Using shorthand, check if a number is a multiple of 4 and print "Multiple of 4" or "Not a multiple"."""
num = 8
print("Multiple of 4") if num % 4 == 0 else print("Not a multiple")
print()

"""18. Create a program that checks whether the given day is a weekday or weekend using if-else conditions."""
day = "Monday"
weekday = ["monday","tuesday","wednesday","thursday","friday"]
weekend = ["saturday","sunday"]
print(f"{day} is weekdays") if day.lower() in weekday else print(f"{day} is weekend")
print()

"""19. Write a program that takes a temperature input and categorizes it into "Cold", "Warm", or "Hot" based on set ranges."""
tem = -10
print("Hot tem") if tem > 40 else print("Warm tem") if 0 < tem < 40 else print("Cool tem")
print()

"""20. Create a program to check if a given number is positive, negative, or zero."""
n = 20
if n > 0:
    print(f"Positive no. = {n}")
elif n == 0:
    print(f"Zero no. = {n}")
else:
    print(f"Negative no. = {n}")
print()

### **Advanced Level:**

"""21. Write a program that checks whether a number is prime or not using if-else."""
n = 2
count = 0
if n > 1:
    for i in range(2,n):
        if n % 2 == 0:
            count += 1
    if count == 0:
        print(f"{n} is a prime no.")
    else:
        print(f"{n} is not a prime no.")
else:
    print(f"{n} is not a prime no.")
print()

"""22. Create a program to determine the grade of a student based on marks and handle different edge cases."""
marks = 78
if marks >= 90:
    print("A+ Grade")
elif marks >= 75:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
elif marks >= 50:
    print("C Grade")
else:
    print("Fail")
print()

"""23. Write a Python program to validate user input: check if the input is a number, and if so, whether it’s odd, even, positive, or negative."""
n = "-10"
if n.isdigit():
    num = int(n)
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    if num > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Not a digit")
print()

"""24. Using nested `if-else`, create a program that categorizes a person’s BMI based on height and weight."""
weight = 60
height = 1.51
bmi = weight / (height**2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
else:
    print("Overweight")
print()

"""25. Create a program that asks for three numbers and prints the largest using nested `if-else`."""
a, b, c = 10, 20, 30

if a > b:
    if a > c:
        print("A is largest")
    else:
        print("C is largest")
else:
    if b > c:
         print("B is largest")
    else:
        print("C is largest")
print()
"""26. Write a program to simulate a simple login system, checking the username and password using `if-elif-else`."""
username = "user1"
password = "pass123"
if username == "user1" and password == "pass123":
    print("Login successful")
elif username == "user1":
    print("Wrong password")
else:
    print("Invalid credentials")
print()

"""27. Create a Python program that evaluates a mathematical expression input by the user and checks if it's valid."""


"""28. Write a program to determine the season based on the current month (input from the user)."""
month = "june"
if month.lower() in ["december","january","february"]:
    print(f"{month} month winter season")
elif month.lower() in ["march","april","may"]:
    print(f"{month} month spring season")
elif month.lower() in ["june", "july", "august"]:
    print(f"{month} month summer season")
elif month.lower() in ["september","october","november"]:
    print(f"{month} month autumn season")
else:
    print("Invalid month")
print()

"""29. Write a Python program that checks if a user-entered year is from the 20th century (1901–2000), 21st century (2001–2100), or earlier."""
year = 1902
if 1901 <= year <= 2000:
    print("20th century")
elif 2001 <= year <= 2100:
    print("21th century")
else:
    print("Invalid year")
print()
"""30. Write a Python program that accepts an employee’s salary and determines the bonus using `if-elif-else` conditions (e.g., different percentages based on salary slabs)."""
salary = float(input("Enter the employee's salary: "))

if salary < 30000:
    bonus = 0.20 * salary  # 20% bonus for salaries below 30,000
elif 30000 <= salary < 50000:
    bonus = 0.15 * salary  # 15% bonus for salaries between 30,000 and 49,999
elif 50000 <= salary < 70000:
    bonus = 0.10 * salary  # 10% bonus for salaries between 50,000 and 69,999
else:
    bonus = 0.05 * salary  # 5% bonus for salaries 70,000 and above

print(f"The bonus for a salary of {salary} is {bonus:.2f}")
