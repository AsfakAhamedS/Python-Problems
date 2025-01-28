### **Python Sets Tasks**

#### **Easy:**
"""1. Create a set of five different name and print it."""
name = {"Luffy","Ace","Sabo"}
print(name)
print()

"""2. Access and print each item in a set using a loop."""
for x in name:
    print(x)
print()

"""3. Add an element to a set."""
name.add("Saanji")
print(name)
print()

"""4. Add multiple elements to a set using `update()`."""
name.update(["Zoro","God Usopp"])
print(name)
print()

"""5. Remove a specific element from a set using `remove()`."""
name.remove("God Usopp")
print(name)
print()

"""6. Remove an element using `discard()`, and try to discard an element that does not exist."""
name.discard("God Usopp")
print(name)
print()

"""7. Remove an arbitrary element from the set using `pop()` and print the updated set."""
remove = name.pop()
print(f"Set = {name} and Remove Element = \"{remove}\"")
print()

"""8. Clear all items from a set using `clear()`."""
name.clear()
print(name)
print()

"""9. Create two sets, find their union, and print it."""
set_A = {1,2,3,4,5}
set_B = {6,7,8,9,10}
set_Union = set_A.union(set_B)
print(set_Union)
set_A = {1,2,3,4,5}
set_B = {6,7,8,9,10}
set_A.update(set_B)
print(set_A)
print()

"""10. Create two sets and find their intersection."""
set_A = {1,2,3,4,5}
set_B = {5,6,7,8,9,10}
set_Inter = set_A.intersection(set_B)
print(set_Inter)
set_A = {1,2,3,4,5}
set_B = {5,6,7,8,9,10}
set_A.intersection_update(set_B)
print(set_A)
print()

#### **Intermediate:**
"""11. Create a set and check if a particular element exists in the set."""
name = {"Luffy","Ace","Sabo"}
if "Zoro" in name:
    print("Yes, Present")
else:
    print("No,  Not present")
print()

"""12. Create two sets and print their difference."""
set_A = {1,2,3,4,5}
set_B = {5,6,7,8,9,10}
set_Diff = set_A - set_B
print(set_Diff)
set_A = {1,2,3,4,5}
set_B = {5,6,7,8,9,10}
set_A.difference_update(set_B)
print(set_A)
print()

"""13. Create two sets and print their symmetric difference."""
set_A = {1,2,3,4,5}
set_B = {5,6,7,8,9,10}
set_Sym = set_A ^ set_B
print(set_Sym)
set_A = {1,2,3,4,5}
set_B = {5,6,7,8,9,10}
set_A.symmetric_difference_update(set_B)
print(set_A)
print()

"""14. Perform a union operation and assign the result to a new set variable."""
set_A = {1,2,3,4,5}
set_B = {6,7,8,9,10}
set_Union = set_A.union(set_B)
print(set_Union)
print()

"""15. Write a program to find if one set is a subset of another."""
set_A = {1,2,3,4,5}
set_B = {1,2,3,4,5,6,7,8,9,10}
set_Sub = set_A.issubset(set_B)
print("Subset = ",set_Sub)
print()

"""16. Write a program to check if two sets are disjoint."""
set_A = {1,2,3,4,5,6}
set_B = {6,7,8,9,10}
set_joi = set_A.isdisjoint(set_B)
print(set_joi)
print()

"""17. Remove duplicates from a list using a set."""
list_dup = [1,2,3,3,4,4,5,6,5]
list_rem = list(set(list_dup))
print(list_rem)
print()

"""18. Create a set and find the length of the set using `len()`."""
set_Len = len(set_A)
print(set_Len)
print()

"""19. Create a set and demonstrate how to use the `issuperset()` method."""
set_A = {1,2,3,4,5,6,7,8,9,10}
set_B = {1,2,3,4,5}
set_Sub = set_A.issuperset(set_B)
print("Super set =", set_Sub)
print()

"""20. Perform a set comprehension that extracts vowels from a string and stores them in a set."""
strings = "Hello world A"
vow = set()
for i in strings:
    if i.lower() in "aeiou":
        vow.add(i)
print(vow)

#### **Advanced:**
"""21. Given two sets, perform all the basic set operations (union, intersection, difference, and symmetric difference) and store the results in a dictionary."""
set_A = {1,2,3,4,5}
set_B = {5,6,7,8,9,10}
set_op = {
    "Union" : set_A.union(set_B),
    "Inter" : set_A.intersection(set_B),
    "Diff." : set_A.difference(set_B),
    "Sym_diff." : set_A.symmetric_difference(set_B)
}
print(set_op)
print()

"""22. Write a program to find common elements in three sets."""
set_A = {1,2,3,4,5}
set_B = {5,6,7,8,9,10}
set_C = {5,6,11,12,13}
set_Com = set_A & set_B & set_C
print(set_Com)
print()

"""23. Given a list of sets, write a program to find the common elements across all sets."""
list_Set = [{1,2,3,4,5},{5,6,7,8,9,10},{5,6,11,12,13}]
set_setcom = set.intersection(*list_Set)
print(set_setcom)
print()

"""24. Write a program that uses sets to find the unique words in a sentence."""
sentence = "this is a test this is only a test"
words = set(sentence.split(" "))
print(words)  # Output: {'this', 'only', 'test', 'a', 'is'}
print()

"""25. Implement a function that accepts a list of tuples and returns a set of unique first elements from each tuple."""
list_tuple = [(1,2),(2,1),(3,3),(1,1),(22,1),(5,3)]
set_unq = set()
for i in list_tuple:
    set_unq.add(i[1])
print(set_unq)
print()

"""26. Create a program that generates random sets of numbers, and calculates their intersections and unions."""
import random

set1 = {random.randint(1, 10) for _ in range(5)}
set2 = {random.randint(1, 10) for _ in range(5)}

print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection:", set1.intersection(set2))
print("Union:", set1.union(set2))
print()


