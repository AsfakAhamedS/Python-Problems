### **Easy Tasks**
"""1. **Print Numbers**: Write a loop to print numbers from 1 to 10."""
i = 1
while i <= 10:
    print(i,end=" ")
    i += 1
print()

"""2. **Sum of Numbers**: Use a loop to calculate the sum of numbers from 1 to 100."""
i = 1
sums = 0
while i <= 100:
    sums += i
    i += 1
print(sums)
print()

"""3. **Multiplication Table**: Print the multiplication table of any number up to 10."""
n = 9
i = 1
while i <= 10:
    print(f"{i} x {n} = {i*n}")
    i += 1
print()

"""4. **Count Even Numbers**: Count and print even numbers between 1 and 20."""
count = 0
for i in range(2,21,2):
        count += 1
        print(f"Count = {count} and Even no = {i}")
print()

"""5. **Reverse Counting**: Print numbers from 10 to 1 in reverse order."""
i = 10
while i >= 1:
    print(i,end=" ")
    i -= 1
print()
print()

"""6. **Factorial**: Calculate the factorial of a number using a loop."""
num = 5
fact = 1
for i in range(1,num+1):
    fact *= i
print(fact)
print()

"""7. **Characters in a String**: Print each character in a string using a loop."""
strs = "Hello World!"
for i in strs:
    print(i,end=" ")
print()
print()

### **Intermediate Tasks**
"""8. **Sum of Digits**: Calculate thec in an integer using a loop."""
num = 15
tot = 0
while num > 0:
    rem = num % 10
    tot = tot + rem
    num //= 10
print(tot)
print()

"""9. **Fibonacci Sequence**: Print the first 10 numbers of the Fibonacci sequence."""
num = 10
x, y = 0, 1
for _ in range(num):
    print(x, end=" ")
    x, y = y, x + y
print()
print()

"""10. **Prime Numbers**: Write a loop to print all prime numbers between 1 and 50."""
n = 50
for i in range(1,n+1):
    if n > 1:
        count = 0
        for j in range(2,i+1):
            if i % j == 0:
                count += 1
        if count == 1:
            print(i,end=" ")
print()
print()

"""11. **Pattern Printing**: Print a right-angled triangle pattern using `*`."""
n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
print()

"""12. **Count Vowels**: Count the number of vowels in a given string."""
strs = "Hello World!"
count = 0
for i in strs:
    if i.lower() in "aeiou":
        count += 1
print(f"Vowels count = {count}")
print()

"""13. **Number Guessing Game**: Implement a number guessing game using a `while` loop."""
"""import random
target = random.randint(1,100)
guess = 0
while guess != target:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < target:
        print("Too low!")
        print(target)
    elif guess > target:
        print("Too high!")
        print(target)
    else:
        print("Correct!")
        print(target)
print()
"""
"""14. **Power Calculation**: Calculate `x^y` using a loop."""
x = 3
y = 2
result = 1
for _ in range(y):
    result *= x
print(f"{x}^{y} = {result}")
print()

"""15. **Sum of Even/Odd Numbers**: Calculate and print the sum of all even and odd numbers up to a given number."""
rang = 10
even = 0
odd = 0
for i in range(1,rang+1):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print(f"Even = {even} and Odd = {odd}")
print()
"""16. **Divisors of a Number**: Find all divisors of a given number using a loop."""
n = 10
for i in range(1, n+1):
    if n % i == 0:
        print(f"Divisor of {n} in {i}")
print()

"""17. **List Reversal**: Reverse a list of numbers using a loop."""
lists = [1,2,3,4,5]
res = []
for i in lists[::-1]:
    res.append(i)
print(res)
print()

"""18. **Palindrome Check**: Check if a given number or string is a palindrome."""
n = 101
out = n
res = 0
while n > 0:
    rem = n % 10
    res = (res * 10) + rem
    n //= 10
if res == out:
    print(res, "Palindrome")
else:
    print(res, " Not Palindrome")
print()

"""19. **Simple Interest Calculation**: Use loops to calculate simple interest for multiple years."""
"""
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))
for t in range(1, time + 1):
    interest = (principal * rate * t) / 100
    print(f"Year {t}: Interest = {interest}")
"""

"""20. **Character Count**: Count the occurrences of each character in a string."""
strs = "Asfak A"
count = 0
for i in strs:
    if strs.isalpha():
        count += 1
    else:
        continue
print(count)
print()

### **Advanced Tasks**
"""21. **Bubble Sort**: Implement the bubble sort algorithm using a loop.
22. **Multiplication Table Grid**: Print a grid with multiplication tables from 1 to 10.
23. **Prime Factorization**: Print the prime factors of a given number.
24. **Square and Cube of Numbers**: Print the square and cube of numbers from 1 to 10 using loops.
25. **Pattern Printing**: Create a diamond pattern with `*`.
26. **GCD Calculation**: Find the greatest common divisor (GCD) of two numbers using a loop.
27. **Unique List Elements**: Write a program to print unique elements from a list using loops.
28. **Generate Fibonacci Series Up to N**: Print the Fibonacci series up to a given number `N`.
29. **Nested Loop Pattern**: Print a number pyramid (nested loop).
30. **Caesar Cipher**: Implement a Caesar cipher encryption using loops."""

