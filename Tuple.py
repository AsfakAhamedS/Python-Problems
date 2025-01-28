### **Easy Level:**
"""1. Create a tuple with different names."""
name = ("Luffy","Ace","Sabo")
print(name)
print()
"""2. Access the third item from a tuple of numbers."""
print(name[2])
print()
"""3. Check if the value `'Ace'` is present in a tuple."""
if "Ace" in name:
    print("Yes, present")
else:
    print("No, not present")
print()
"""4. Find the length of a tuple containing 3 elements."""
print(f"Length of name = \"{len(name)}\"")
print()
"""5. Create a tuple with just one element and print its type."""
nam = ("Luffy",)
print(type(nam))
print()
"""6. Unpack a tuple containing three values into three variables."""
name1,name2,name3 = name
print(f"Nanme 1 = {name1}, Name 2 = {name2} and Name 3 = {name3}")
print()
"""7. Access the last element of a tuple without using its index."""
print(f"Last element = {name[-1]}")
print()
"""8. Loop through a tuple of colors and print each item."""
for i in name:
    print(i)
print()
"""9. Concatenate two tuples containing numbers and print the result."""
a = (1,2,3,4,5)
b = (6,7,8,9,10)
c = a + b
print(c)
print()

"""10. Count how many times the value `5` appears in the tuple `(1, 2, 5, 7, 5, 3, 5)`."""
tup = (1, 2, 5, 7, 5, 3, 5)
print(f"\'5\' apper count = {tup.count(5)} ")
print()

### **Intermediate Level:**
"""11. Create a tuple from user input and print the tuple."""
#value = input("Enter the value: ")
#tup = tuple(value.split(", "))
#print(tup)
#print()
"""12. Update a tuple by replacing its second element with a new value (Hint: Use conversion to a list)."""
name = ("Luffy", "Ace", "Zoro")
print(f"Before change = {name}")
re_Place = list(name)
re_Place[2] = "Sabo"
name = tuple(re_Place)
print(f"After change = {name}")
print()
"""13. Unpack a tuple into variables but skip the first two values using a placeholder variable."""
data = (10, 20, 30, 40)
_, _, x, y = data
print(_,x, y,_)
print()
"""14. Find the index of the value `'Ace'` in a tuple."""
print(f"Position no. of \"Ace\" = {name.index('Ace')}")
print()
"""15. Join two tuples of student names, but exclude duplicate values from the second tuple."""
name1 = ("Luffy", "Ace", "Sabo")
name2 = ("Sabo", "Zoro", "Saanji", "God Usopp")
re_Place = list(name2)
print(f"Before Name 1 = {name1} and Name 2 = {name2}")
for i in name1:
    if i in re_Place:
        re_Place.remove(i)
name2 = tuple(re_Place)
print(f"After Name 1 = {name1} and Name 2 = {name2}")
print()

"""16. Write a program to unpack a tuple of 5 elements into three variables, with the last two elements grouped into one variable."""
name = ("Luffy", "Ace", "Sabo", "Zoro", "Saanji", "God Usopp")
brother1, brother2, brother3, *teammate = name
print(teammate)
print()
"""17. Use a loop to print each item in the tuple along with its index."""
for i in range(len(name)):
    print(f"Name = {name[i]} and their Index no. = {i}")
print()
"""18. Write a function that takes a tuple as input and returns a new tuple with the first and last elements swapped."""
def swap_ends(t):
    return t[-1:] + t[1:-1] + t[:1]

print(swap_ends((1, 2, 3, 4)))
print()

"""19. Write a program to reverse a tuple (e.g., `(1, 2, 3)` becomes `(3, 2, 1)`)."""
tup = (1,2,3,4,5)
rev = tup[::-1]
print(rev)
print()
"""20. Merge two tuples `(1, 2, 3)` and `(4, 5, 6)` and then sort the result."""
a = (5, 4, 3)
b = (1, 2, 6)
c = tuple(sorted(a+b))
print(c)
print()

### **Advanced Level:**
"""21. Write a program to find the largest and smallest element in a tuple of integers."""
print(f"Largest element = {c[-1]} and Smallest element = {c[0]}")
print()

"""22. Create a tuple with mixed data types (e.g., strings, integers, lists) and access an element inside the list within the tuple."""
mix = ("Ace", 21, [5.1, 5.10])
print(mix[2][1])
print()
"""23. Write a program to convert a tuple of strings into a single string (e.g., `('a', 'b', 'c')` becomes `'abc'`)."""
a = ('a', 'b', 'c')
b = ""
for i in a:
    b += i
print(f"Tuple = {a} and String = {b}")
chars = ('a', 'b', 'c')
result = ' '.join(chars)
print(result)
print()
"""24. Write a function that returns the most frequent element in a tuple."""
tup = (1, 2, 5, 7, 5, 3, 5)
fre = max(tup, key=tup.count)
print(fre)
print()
"""25. Given a tuple, write a program to remove any elements that are repeated."""
re_Place = list(tup)
for i in range(len(re_Place)):
    if fre in re_Place:
        re_Place.remove(fre)
re_Place.append(fre)
tup = tuple(sorted(re_Place))
print(tup)
numbers = (1, 2, 3, 2, 4, 5, 3)
unique_numbers = tuple(set(numbers))
print(unique_numbers)
print()

"""26. Write a program to rotate the elements of a tuple by one position to the left (e.g., `(1, 2, 3)` becomes `(2, 3, 1)`)."""
t = (1, 2, 3, 4, 5)
rotated = t[1:] + t[:1]
print(rotated)
print()

"""27. Write a program to split a tuple of 10 elements into two tuples of equal length."""
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
le = len(a) // 2
fh = a[:le]
lh = a[le:]
print(fh,lh)
print()
"""28. Write a program to find all unique elements in a tuple by using the `count` method."""
tup = (1, 10, 1, 2, 5, 6, 7, 2, 5, 3, 5)
for i in range(len(tup)):
    if tup.count(i) == 1:
        print(f"{i} is unique")
print()
"""29. Create a function that takes a tuple of tuples (e.g., `((1, 2), (3, 4), (5, 6))`) and flattens it into a single tuple (i.e., `(1, 2, 3, 4, 5, 6)`)."""
a = ((1, 2), (3, 4), (5, 6))
b = list(a)
c = []
for i in b:
    for j in i:
        c.append(j)
print(tuple(c))
print()
"""30. Write a program to join multiple tuples together and then remove any duplicate values."""
a = (1,2,3)
b = (3,4,5,6)
c = ( 5,6,7,8,9)
d = set(a+b+c)
print(tuple(d))


a={1,2,3,4}
b={4,5,6}
s=a.intersection_update(b)
print(a)