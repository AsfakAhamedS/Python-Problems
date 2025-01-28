### **Python Dictionaries Tasks**

#### **Easy:**
"""27. Create a dictionary with three key-value pairs and print it."""
detail = {
    "Name1" : "Luffy",
    "Name2" : "Ace",
    "Name3" : "Sabo"
}
print(detail)
print()

"""28. Access and print a specific value using its key."""
print(detail["Name1"])
print(detail["Name2"])
print(detail["Name3"])
print()

"""29. Add a new key-value pair to the dictionary."""
detail["Name4"] = "Saanji"
detail.update({"Name5" : "Zoro"})
print(detail)
print()

"""30. Change the value of an existing key in a dictionary."""
detail["Name4"] = "God Usopp"
detail.update({"Name5" : "Chopper"})
print(detail)
print()

"""31. Remove a key-value pair using the `pop()` method."""
detail.pop("Name5")
print(detail)
print()

"""32. Remove the last inserted key-value pair using `popitem()`."""
detail.popitem()
print(detail)
print()

"""33. Copy a dictionary using the `copy()` method."""
det_Copy = detail.copy()
print(f"Original = {detail}\nCopy = {det_Copy}")
print()

"""34. Create a nested dictionary with two levels and access an inner dictionary value."""
detail = {
    "team1" : {
        "name1" : "luffy",
        "name2" : "god usopp"},
    "team2" : {
        "name1" : "ace",
        "name2" : "saanki"},
    "team3" : {
        "name1" : "sabo",
        "name2" : "zoro"},

}
print(detail["team1"]["name2"])
print()

"""35. Loop through a dictionary to print all keys."""
for i in detail:
    print(i)
#for i in detail.keys():
#    print(i)
print()

"""36. Loop through a dictionary to print all values."""
for i in detail:
    print(detail[i])
#for i in detail.values():
#    print(i)
print()

#### **Intermediate:**
"""37. Create a dictionary and use the `get()` method to safely access a key that may or may not exist."""
print(detail.get("team1","Not fount"))
print(detail.get("team4"," Not fount"))
print()

"""38. Merge two dictionaries into a new dictionary."""
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
merged_dict = {**dict1, **dict2}
print(merged_dict)

print()

"""39. Write a program to remove a key from a dictionary if it exists."""
person = {"name": "Alice", "age": 25}
if "age" in person:
    del person["age"]
print(person)
print()

"""40. Write a program that counts the frequency of each character in a string using a dictionary."""
string = "hello world"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

string = "hello world"
char_count = {}
for char in string:
    char_count.update({char:"1"})
print(char_count)