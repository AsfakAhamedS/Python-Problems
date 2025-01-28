### **Easy:**
"""1. Perform addition on two numbers using the `+` operator."""
a, b = 10, 20
print(f"Addition {a} + {b} = {a+b}")
print()
"""2. Subtract one number from another using the `-` operator."""
#a, b = 10, 20
print(f"Subtraction {a} - {b} = {a-b}")
print()
"""3. Multiply two numbers using the `*` operator."""
#a, b = 10, 20
print(f"Multiplication {a} * {b} = {a*b}")
print()
"""4. Divide two numbers using the `/` operator."""
#a, b = 10, 20
print(f"Division {a} / {b} = {a/b}")
print()
"""5. Find the remainder of a division using the modulus `%` operator."""
#a, b = 10, 20
print(f"Remainder {a} % {b} = {a%b}")
print()
"""6. Use the `**` operator to calculate 3 raised to the power of 4."""
a, b = 3, 4
print(f"Power {a} ** {b} = {a**b}")
print()
"""7. Perform integer division using the `//` operator."""
a, b = 10, 20
print(f"Floor division {a} // {b} = {a//b}")
print()
"""8. Assign a value to a variable using the `=` operator."""
#a, b = 10, 20
print(f"Assign a = {a} and b = {b}")
print()
"""9. Add 5 to a variable using `+=`."""
a = 10
a += 5
print(f"Add a += b op = {a}")
print()
"""10. Subtract 2 from a variable using `-=`."""
a = 10
a -= 2
print(f"Sub a -= b op = {a}")
print()

### **Moderate:**
"""11. Multiply a variable by 3 using `*=`."""
a = 10
a *= 3
print(f"Multiply a *= b op = {a}")
print()
"""12. Divide a variable by 2 using `/=`."""
a = 10
a /= 2
print(f"divide a /= b op = {a}")
print()
"""13. Use comparison operators to check if two numbers are equal (`==`)."""
a, b = 10, 10.0
if a == b:
    print("a={} and b={} both are equal.".format(a,b))
else:
    print("Not equal")
print()
"""14. Use comparison operators to check if one number is greater than the other (`>`)."""
a, b = 10, 20
if a > b:
    print("a=%d greater than b=%d"%(a,b))
else:
    print("b=%d greater than a=%d"%(b,a))
print()
"""15. Check if one number is less than or equal to another (`<=`)."""
a, b = 10, 20
if a <= b:
    print("a=%d lesser than b=%d"%(a,b))
else:
    print("b=%d lesser than a=%d"%(b,a))
print()
"""16. Use `!=` to compare two strings and check if they are not equal."""
a, b = 10, 20
if a != b:
    print("a=%d not equal b=%d"%(a,b))
else:
    print("b=%d equal a=%d"%(b,a))
print()
"""17. Use the `and` operator to check if both conditions are true: 5 > 3 and 8 < 10."""
a, b = 10, 20
if a < b and b > a:
    print("Both condition \"True\"")
else:
    print("Both condition \"False\"")
print()
"""18. Use the `or` operator to check if either of two conditions is true."""
if a < b or b < a:
    print("Either one condition \"True\"")
else:
    print("Both condition \"False\"")
print()
"""19. Use the `not` operator to reverse a Boolean value."""
num = ""
if not num:
    print("True")
else:
    print("False")
print()
"""20. Check if an element is present in a list using the `in` operator."""
name = "Ace is most popular character in one piece"
if "Ace" in name:
    print(f"\"Ace\" present in name \"{name}\"")
else:
    print("Not present")
print()

### **Challenging:**
"""21. Check if an element is not in a list using the `not in` operator."""
name = ["Ace","Ashzul","Luffy","Zoro"]
ch = "Saanji"
if ch not in name:
    print(f"Yes, \"{ch}\" not present in list {name}")
else:
    print(f"No, \"{ch}\" present it. {name}")
print()

"""22. Write a program that compares three numbers and prints the largest using comparison operators."""
a, b, c = 10, 20, 30
if a > b and a > c:
    print(F"{a} is greatest")
elif b > a and b > c:
    print(F"{b} is greatest")
else:
    print(F"{c} is greatest")
print()
"""23. Create a program that swaps the values of two variables using assignment operators."""
a, b = 10, 20
print(f"Before swap a = {a} and b = {b}",end="")
a, b = b, a
print(f"After swap a = {a} and b = {b}")
print()
"""24. Write a program that uses the `and` operator to check if a number is divisible by both 2 and 3."""
num = 10
if num % 2 == 0 and num % 3 == 0:
    print("Yes, it's divisible.")
else:
    print("Not divisible.")
print()
"""25. Use `or` to check if a number is divisible by either 5 or 7."""
num = 10
if num % 5 == 0 or num % 7 == 0:
    print("Yes, it's divisible.")
else:
    print("Not divisible.")
print()
"""26. Create a program that finds the difference between two numbers and checks if the result is positive using comparison operators."""
a, b = 10, 20
print(f"a = {a}, b = {b} and diff = {a-b} and check \"{a-b > 0}\"")
print()
"""27. Write a program that checks if a user-input number is even or odd using modulus and comparison operators."""
Input = 10 #user input
if Input % 2 == 0:
    print("It's Even number")
else:
    print("It's Odd number")
print()
"""28. Use assignment operators to accumulate the sum of numbers from 1 to 10."""
n = 10
res = 0
for i in range(1,n+1):
    res += i
print("sum of numbers from 1 to 10 = ",res)
print()
"""29. Write a program that finds the product of all elements in a list using a loop and the `*=` assignment operator."""
n = [1,2,3,4,5]
res = 1
for i in n:
    res *= i
print("Product of numbers in list = ",res)
print()
"""30. Write a program to check if a string is a palindrome using membership operators."""
#Built-in Function
n = "121"
temp = n
if temp in n[::-1]:
    print("Yes, It's palindrome.")
else:
    print("Not a palindrome.")
print()
n = 1005001
temp = n
res = 0
while temp != 0:
    rem = temp % 10
    res = (res *  10) + rem
    temp //= 10
if res == n:
    print("Yes, It's palindrome.Without Built-in function.")
else:
    print("Not a palindrome.Without Built-in function.")
print()
### **Advanced:**
"""31. Use nested conditions with `and`, `or`, and comparison operators to check if a number is within a certain range (e.g., between 10 and 50)."""
num = 20
if num <= 50:
    if num >= 10:
        print(f"{num} within a certain range between 10 and 50")
    else:
        print(f"{num} without a certain range between 10 and 50")
else:
    print(f"{num} without a certain range between 10 and 50")
print()
"""32. Write a program that calculates the factorial of a number using a loop and assignment operators."""
n = 5
res = 1
for i in range(1,n+1):
    res *= i
print("Factorial = ",res)
print()
"""33. Use the `not` operator to implement a toggle switch that flips between True and False."""
switch = False
switch = not switch
print(switch)
print()
"""34. Create a program that validates a user's age input (between 18 and 60) using comparison operators."""
Age = 60
if 18 <= Age <= 60:  #Age >= 18 and Age <= 60
    print("Eligible")
else:
    print("Not eligible")
print()
"""35. Write a program that checks if two lists have any common elements using membership operators."""
a = [1,2,3,4,5]
b = [5,6,7,8,9]
for i in a:
    if i in b:
        print(f"Common element is {i}")
print()
"""36. Write a program that checks if a set is a subset of another using membership operators."""
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
if set_a.issubset(set_b):
    print(f"{set_a} is a subset of {set_b}")
else:
    print(f"{set_a} is not a subset of {set_b}")
# Define two sets
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
is_subset = True
for elem in set_a:
    if elem not in set_b:
        is_subset = False
        break
if is_subset:
    print(f"{set_a} is a subset of {set_b}")
else:
    print(f"{set_a} is not a subset of {set_b}")
print()
"""37. Use arithmetic and comparison operators to calculate and compare the areas of two rectangles."""
l1, l2, w1, w2 = 5, 3, 10, 15
area_1, area_2 = l1*w1, l2*w2
if area_1 > area_2:
    print(f"area1 = {area_1} greater than area2 = {area_2}")
else:
    print(f"area2 = {area_2} greater than area1 = {area_1}")
print()
"""38. Write a program to sort a list of numbers and check if each number is greater than the previous one using comparison operators."""
a = [7,2,4,3,0,1]
#a = ["aaaaa","a","aaa","aa"]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i] >= a[j]:      #if len(a[i]) >= len(a[j])
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
for i in range(1,len(a)):
    if a[i] < a[i-1]:
        print("Fails")
print(a)
print()
"""39. Write a program to evaluate a mathematical expression (like 3 + 2 * (5 ** 2)) and output the result."""
print(3 + 2 * (5 ** 2))
print()
"""40. Create a program that prompts for a password, and uses logical operators to ensure it meets multiple conditions (length, special characters, etc.)."""
a= "sheiCk@#123"
special_characters = "!@#$%^&*()-+"
if len(a) >= 8:
    u=l=s=False
    for i in a:
        if i in special_characters:
            s = True
        elif 'A' <= i and i <= 'Z':
            u =True
        elif 'a' <= i and i <= 'z':
            l = True

    if s and u and l:
        print("Password too Strong")
    else:
        print("Password too weak")

else:
    print("Password too short")
print()
a="2"
if a <= "1" and a <= "10":
    print("kd")
else:
    print("d")
### **Expert:**
"""41. Write a program that uses assignment operators to solve a linear equation (like 2x + 3 = 11).
42. Implement a program that checks if a given number is prime using comparison operators.
43. Create a program that simulates a simple calculator using all arithmetic and assignment operators.
44. Use logical operators to check if a number is within one of multiple ranges (e.g., 10-20 or 30-40).
45. Write a program to simulate a basic login system using `and`, `or`, and comparison operators.
46. Write a function that takes two numbers and returns a tuple with results from all arithmetic operations.
47. Create a program that uses a loop and assignment operators to find the greatest common divisor (GCD) of two numbers.
48. Write a program to find all the even numbers in a list and check if their sum is greater than 100 using logical operators.
49. Implement a program that solves quadratic equations using the quadratic formula and comparison operators.
50. Write a program that takes user input, converts it into an arithmetic expression (like "3 + 4 * 2"), and evaluates it dynamically using operators."""
