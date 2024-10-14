### **Basic Level:**

"""1. **Task 1:** Create a string variable with your name and print it."""
name = "Ace"
print(name)
print()

"""2. **Task 2:** Print the length of a given string."""
NameLength = len(name)
print(f"Name length is {NameLength}")
print()

"""3. **Task 3:** Convert a string to uppercase."""
upCase = name.upper()
res = "My name is \"Upper Case\" {}"
print(res.format(upCase))
print()

"""4. **Task 4:** Convert a string to lowercase."""
loCase = name.lower()
res = "My name is \"Upper Case\" {}".format(loCase)
print(res)
print()

"""5. **Task 5:** Check if a string contains a particular word ("Python") using the `in` keyword."""
word = "Most popular language is python programming."
if "python" in word:
    print("yes, python presented in \"word\"")
else:
    print("No, python is not presented in \"word\"")
print()

"""6. **Task 6:** Slice the first 5 characters of a string."""
#word = "Most popular language is python programming."
print("Slicing the characters in word ","\"",word[13:22],"\"")
print()

"""7. **Task 7:** Slice the last 3 characters of a string."""
#word = "Most popular language is python programming."
print("Slicing the last characters in word ","\"",word[-12:-1],"\"")
print()

"""8. **Task 8:** Remove any leading or trailing spaces from a string."""
spaces = "     A C E    "
print("Remove the space in ","\"",spaces.strip(),"\"")
print()

"""9. **Task 9:** Concatenate two strings (e.g., "Hello" and "World")."""
first = "Hello"
second = "World!"
print("Concatenate = ",first+" "+second)
print()

"""10. **Task 10:** Check if a string is entirely numeric.""" #isdigit() keyword is used to check numeric value or not.
strings = "123456789"
strings1 = "Ace"
print("Is a numeric value = ","\"",strings.isdigit(),"\"","and Is a numeric value = ","\"",strings1.isdigit(),"\"")
print()

"""11. **Task 11:** Check if a string contains only alphabets.""" #isalpha() keyword is used to check alphabets char or not.
strings2 = "Ace11112002"
strings3 = "Ace"
print("Is only contain alphabets = ","\"",strings2.isalpha(),"\"","and Is only contain alphabets = ","\"",strings3.isalpha(),"\"")
print()

"""12. **Task 12:** Replace all occurrences of a substring ("Java") with another substring ("Python")."""
subString = "Java is a most popular language"
tem1 = subString
tem2 = subString.replace("Java","Python")
print(f"Before \"{tem1}\" \nAfter \"{tem2}\"")
print()

### **Intermediate Level:**
"""13. **Task 13:** Reverse a given string using slicing.""" # ::-1 this used to reverse
#subString = "Java is a most popular language "
print("Reverse using slicing = ",subString[::-1])
print()

"""14. **Task 14:** Check if a string is a palindrome (reads the same forward and backward)."""
str1 = "malayalam"
str2 = "malayalam"
t1 = str1[:]
t2 = str2[::-1]
if t1 == t2:
    print("Palindrome","\"",t1,"\"")
else:
    print("Not Palindrome","\"",t2,"\"")
string = "madam"
print(string == string[::-1])
print()

"""15. **Task 15:** Use string formatting to insert values into a sentence. Example: "My name is {name} and I am {age} years old."""
name = "Ace"
age = 21
print(f"My name is {name} and I am {age} years old.")
print()

"""16. **Task 16:** Extract the domain name from an email address (e.g., "someone@gmail.com" → "gmail.com")."""
email = "ace@gmail.com"
tem3 = email.split("@")[1]
print(f"Extract domain \"{tem3}\"")
print()

"""17. **Task 17:** Count the number of occurrences of a specific character in a string.""" #count() keyword is used to count a character in string
strings4 = "asfak ahamed s"
count = 0
for i in strings4:
    if i == "a":
        count = count + 1
print("Without built-in function = ",count,"and with built-in function = ",strings4.count("s"))
print()

"""18. **Task 18:** Check if a string starts with a certain prefix (e.g., "Hello").""" #startswith keyword check which word starting in string.
string = "Hello, World!"
print(string.startswith("Hello"))
print()

"""19. **Task 19:** Check if a string ends with a specific suffix (e.g., ".com")."""
#string = "Hello, World!"
print(string.endswith("World!"))
print()

"""20. **Task 20:** Find the index of the first occurrence of a character in a string.""" #index() keyword used to find the index in string.
#string = "Hello, World!"
print(string.index('H'))
print()

"""21. **Task 21:** Remove all vowels from a string."""
#string = "Hello, World!"
vowel = "aeiouAEIOU"
tem4 = ""
for i in string:
    if i not in vowel:
        tem4 = tem4 + i
print(tem4)
print()

"""22. **Task 22:** Use escape characters to print a string that contains both single and double quotes."""
name = "Ace"
age = 21
print(f"My name is \"{name}\" and my age is \'{age}\'")
print()

"""23. **Task 23:** Capitalize the first letter of each word in a sentence."""
strings5 = "ace"
print(strings5.capitalize())
print(strings5.title())
print()


"""24. **Task 24:** Use the `.split()` method to split a sentence into a list of words."""
strings6 = "Ace and Ashzul"
print(strings6.split("and"))
print()

"""25. **Task 25:** Use the `.join()` method to join a list of words into a sentence."""
strings7 = ['Ace','Ashzul']
print(' '.join(strings7))
print()

"""26. **Task 26:** Convert a string to boolean and check if it's True or False. Try converting "True", "False", "0", and an empty string."""
print(bool("True"))   # True
print(bool("False"))  # True
print(bool("0"))      # True
print(bool(""))       # False
print()
### **Advanced Level:**
"""27. **Task 27:** Format a string using f-strings and include calculations (e.g., "The sum of 5 and 6 is {5+6}")."""
a = 5
b = 10
strings8 = "The sum of {0} and {1} is {2}"
print(strings8.format(a,b,a+b))
print()

"""28. **Task 28:** Remove all digits from a string."""
strings9 = "Ace007"
num = "0123456789"
tem5 = ""
for i in strings9:
    if i not in num:
        tem5 += i
print(tem5)
no_digits = ''.join([i for i in strings9 if not i.isalpha()])
print(no_digits)
print()

"""29. **Task 29:** Write a function that takes a string and returns the longest word."""
def lword(a,b):
    if len(a) > len(b):
        return f"Longest string {a}"
    elif len(a) == len(b):
        return f"Both equal length string {a}"
    else:
        return f"Longest string {b}"
a = "Ace"
b = "Ashzul"
print(lword(a,b))
print()
strings10 = "Mass hero ashzul"
l = strings10.split()
tem6 = ""
for i in l:
    if len(i) >= len(tem6):
        tem6 = i
print(f"Longest word in a sentence \"{tem6}\"")
print()

"""30. **Task 30:** Write a function that checks if a string contains only alphanumeric characters."""
strings11 = "Ace007"
print(strings11.isalnum())
print()

"""31. **Task 31:** Create a string that repeats a specific word n times (e.g., "PythonPythonPython" if n=3)."""
#strings11 = "Ace007"
print(strings11 * 3)
print()

"""32. **Task 32:** Implement a function that trims a string to the nearest word limit (e.g., cutting off after 100 characters but ensuring not to cut in the middle of a word)."""
def trim_to_word_limit(text, limit):
    if len(text) <= limit:
        return text
    trimmed = text[:limit].rsplit(' ', 1)[0]
    return trimmed

print(trim_to_word_limit("Python programming is fun", 20))
print()

"""33. **Task 33:** Write a function that counts how many times each vowel appears in a string."""
s = "Asfak Ahamed S and Ace and Ashzul"
vowel ="aeiouAEIOU"
count = 0
for i in s:
    if i in vowel:
        count += 1
print("Vowels = ",count)
print()

"""34. **Task 34:** Use the `.translate()` method to remove punctuation from a string."""
import string
sentence = "Hello, World!"
translator = str.maketrans('', '', string.punctuation)
print(sentence.translate(translator))
print()

"""35. **Task 35:** Write a function that converts a sentence into camel case (e.g., "hello world" → "helloWorld")."""
def case(a):
    b = a.split(" ")
   # res = ' '.join(b[1:])
   # return b[0].lower() + " " + res.title()
    return b[0].lower() + " " + ' '.join(b.capitalize() for b in b[1:])

a = "Ace is a hero"  #Camel Case  = ace Ashzul - Each word starting with capital letter, except first word
print(case(a))       #Pascol case = Ace Ashzul - Each word starting with capital letter
print()              #Snake Case  = ace_ashzul - Each word separated by underscore

"""36. **Task 36:** Implement a string encryption function using a simple Caesar cipher (shift each character by 3 positions)."""

"""37. **Task 37:** Write a function to format a large number with commas as thousand separators."""
number = 100000000
print(f"{number:,}")
print()

"""38. **Task 38:** Check if a string contains balanced parentheses."""

"""39. **Task 39:** Write a function to convert a string representing a binary number to an integer."""
a = "0011"
print(int(a,2))
print()

"""40. **Task 40:** Write a program that extracts hashtags from a tweet-like string."""
tweet = "I love #Python and #coding"
hashtags = [word for word in tweet.split() if word.startswith('#')]
print(hashtags)
"""sp= tweet.split(" ")
for i in sp:
    if i.startswith("#"):
        print(i) """
print()

"""41. **Task 41:** Check if two strings are anagrams of each other."""
a = "Ace"
b = "Cea"
if len(a) == len(b):
    c = sorted(a.lower())
    d = sorted(b.lower())
    if c == d:
        print("Anagram ")
else:
    print("Not a anagram.")
print()

"""42. **Task 42:** Implement a function that checks if a string contains valid email addresses."""

"""43. **Task 43:** Write a function that converts a sentence into its acronym (e.g., "As Soon As Possible" → "ASAP")."""
def fun(a):
    b = a.split(" ")
    temp = ""
    for i in b:
        temp = temp + i[0].upper()
    print(temp)
    print()
a = "As Soon As Possible"
fun(a)

"""44. **Task 44:** Implement a custom sorting algorithm that sorts a list of strings based on their length."""
a = ["Ashzul","Asfak","asdfghj","Ace","a","ace"]
#b = sorted(a)
#print(b)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if len(a[i]) >= len(a[j]):
            tem=a[i]
            a[i]=a[j]
            a[j]=tem
print(a)
b = [10,1,2,0,14,5,6,3,0]
for i in range(0,len(b)):
    for j in range(i+1,len(b)):
        if b[i] >= b[j]:
            tem = b[i]
            b[i] = b[j]
            b[j] = tem
print(b)
print()

"""45. **Task 45:** Use string formatting to align text in a table-like structure (e.g., left-align, right-align, and center)."""
print(f"{'Name':<10} {'Age':^5} {'Country':>10}")
print(f"{'Asfak':<10} {25:^5} {'India':>10}")
print()

"""46. **Task 46:** Find the longest common prefix in an array of strings."""

"""47. **Task 47:** Write a function that removes duplicate characters from a string.
48. **Task 48:** Write a program to generate all possible substrings of a string.
49. **Task 49:** Implement a string compression function that replaces consecutive repeating characters with the character followed by the number of repetitions (e.g., "aabbccc" → "a2b2c3").
50. **Task 50:** Write a function that identifies if a string is a valid password (contains at least one uppercase letter, one lowercase letter, one number, and one special character).

These tasks will give you practical experience with Python strings and booleans, gradually moving from simple to more complex challenges. Let me know if you need explanations for any task!
"""

s = "hello"
encoded = s.encode()
decoded = encoded.decode('utf-8')
print(encoded,decoded)
s = "g"
if not s:
    print("Empty string")
