### **Easy:**
"""1. Create a list of 5 names and print the list."""
name = ["Luffy","Ace","Sabo","Saanji","Zoro"]
print(name)
print()

"""2. Access and print the first and last items from a list."""
print(f"First element = \"{name[0]}\" and Last element = \"{name[-1]}\"")
print()

"""3. Change the second item in the list to a different value."""
name[1]="Portgas D Ace"
print(name)
print()

"""4. Add a new item to the end of the list using `append()`."""
name.append("Nami")
print(name)
print()

"""5. Insert an item at the second position in a list using `insert()`."""
name.insert(5,"Usopp")
print(name)
print()

"""6. Remove an item from the list using `remove()`."""
name.remove("Nami")
print(name)
print()

"""7. Use `pop()` to remove the last item from a list and print it."""
name.pop()
print(name)
print()

"""8. Delete the third item in the list using `del`."""
del name[4]
del name[3]
print(name)
print()

"""9. Clear all items in the list using `clear()`."""
name.clear()
print(name)
print()

### **Intermediate:**
"""10. Print the length of a list using `len()`."""
name = ["Monkey D. Luffy", "Portgas D. Ace", "Sabo", "Zoro", "Saanji", "God Usopp"]
name_Len = len(name)
print(f"Length of name = {name_Len}")
print()

"""11. Reverse the order of a list using `reverse()`."""
name.reverse()
print(name)
print()

"""12. Sort a list of numbers in ascending and descending order using `sort()`."""
name.sort()
print(f"Ascending order = {name}")
name.sort(reverse=True)
print(f"Descending order = {name}")
print()

"""13. Use list comprehension to create a new list that contains only the even numbers from an existing list of integers."""
old_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
new_list = [old_list[x] for x in range(len(old_list)) if old_list[x] % 2 == 0]
print(f"Old list = {old_list} \nNew list = {new_list}")
print()

"""14. Join two lists together using `extend()` and print the result."""
odd = [1,3,5,7,9]
even = [2,4,6,8]
odd.extend(even)
print(odd)
print()

"""15. Create a copy of a list using `copy()` and modify the copy without affecting the original."""
jun = ["Monkey D. Luffy", "Portgas D. Ace"]
sen = jun.copy()
sen.append("Sabo")
print(f"Original = {jun} \nCopy and Modify = {sen}")
print()

"""16. Check if an item is in the list using the `in` keyword, and print a message if it is."""
name = ["Monkey D. Luffy", "Portgas D. Ace", "Sabo", "Zoro", "Saanji", "God Usopp"]
if "God Usopp" in name:
    print("Yes, It present.")
else:
    print("No, It not present.")
print()

"""17. Use `not in` to check if an item is not in the list, and print a message if it isn’t."""
if "God usopp" not in name:
    print("No, It not present.")
else:
    print("Yes, It present.")
print()

"""18. Iterate over a list using a `for` loop and print each item."""
for x in name:
    print(x,end=", ")
print()
"""19. Use a `while` loop to loop through the list and print each item."""
x=0
while x < len(name):
    print(name[x], end=", ")
    x += 1
print()
"""20. Remove duplicates from a list and print the result."""
print()
numbers = [1,2,3,1,4,5,2,6,7,3,8,9,4]
unique_list = []

for num in numbers:
    is_duplicate = False
    for unique_num in unique_list:
        if num == unique_num:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_list.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique_list)
#num = [1,2,3,1,1,2,2,3,4,4,5,6,6,6]
#un = list(set(num))
#print(un)
"""
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list) """
print()

### **Advanced:**
"""21. Create a nested list (a list inside another list) and access an element from the inner list."""
in_list = [1,2,[3,4,5,[6,7]],8,9,10]
print(in_list[2][3][1])
print()

"""22. Use list comprehension to create a list of squares of numbers from 1 to 10."""
square = []
for i in range(1,10+1):
    square.append(i**2)
square_1 = [x**2 for x in range(1,10+1)]
print(square)
print(square_1)
print()

"""23. Create a list of tuples, where each tuple contains a number and its square (e.g., `(1, 1), (2, 4)`)."""
list_tuple = [(x,x**2) for x in range(1,10+1)]
print(list_tuple)
print()
"""24. Write a function that takes a list of numbers and returns a list with only the prime numbers."""
def prime(number1):
    if number1 == 1:
        return False
    for x in range(2, number1):
        if number1 % x == 0:
            return False
    return True
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
prime_list = [number for number in n if prime(number)]
print(prime_list)
print()
"""25. Write a function to find the intersection of two lists (common elements)."""
n1 = [1,2,3,4,5]
n2 = [4,5,6,7,8]
commom = list(set(n1).intersection(set(n2)))
print(commom)
print()
"""26. Create a program that sorts a list of dictionaries by a specific key."""
detail = [{"name":"Ace","Age":21},{"name":"Sabo","Age":20},{"name":"luffy","Age":19}]
print(detail)
print()

"""27. Given a list of strings, sort the list by the length of each string."""
strings = ["Monkey D. Luffy", "Portgas D. Ace", "Sabo", "Zoro", "Saanji", "God Usopp"]
strings.sort(key=len)
print(strings)
print()
"""28. Write a program that finds the second-largest number in a list."""
numbers = [10, 20, 4, 45, 99,45]
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
print(unique_numbers[1])
print()
"""29. Write a function to merge two lists by alternating elements from each list."""
def merge_alternating(list1, list2):
    merged_list = []  # Create an empty list to store the merged result
    # Get the length of the shorter list to avoid index out of range
    min_length = len(list1) if len(list1) < len(list2) else len(list2)

    # Alternate elements from both lists
    for i in range(min_length):
        merged_list.append(list1[i])  # Add element from list1
        merged_list.append(list2[i])  # Add element from list2

    # If one list is longer, add the remaining elements
    for i in range(min_length, len(list1)):
        merged_list.append(list1[i])  # Add remaining elements from list1
    for i in range(min_length, len(list2)):
        merged_list.append(list2[i])  # Add remaining elements from list2

    return merged_list

# Example usage
list1 = [1, 3, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
merged_result = merge_alternating(list1, list2)
print(merged_result)
print()

"""30. Use list comprehension to flatten a list of lists (e.g., `[[1, 2], [3, 4]]` to `[1, 2, 3, 4]`)."""
n = [[1, 2], [3, 4]]
n1 = []
for i in n:
    for j in  i:
        n1.append(j)
print(n1)
