# PRINTING TO CONSOLE
"""
print("Hello World!")
"""

# PRINTING A SHAPE
"""
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
"""

# VARIABLES AND DATA TYPES
"""
character_name = "John" # string, float, int, bool
character_age = 35
character_digits = 42.7
truth = True
print("There was a man named", character_name, "and he was", character_age, "years old!")
print("There was a man named " + character_name + " and he was " + str(character_age) + " years old!")
"""

# STRINGS
"""
print("This is a string")
print("Hi\nThis is on a new \"line\"")
phrase = "Hello There"
print(phrase.lower()) # upper(), isLower(), isUpper(), len(string), index("character"), replace("old","new")
"""

# NUMBERS
"""
print(3+2) # +, -, *, /, %, ** - pow
num = -7
print(abs(num)) # pow(num, power), max(num1, num2), min(num1, num2), round(num)
from math import * # floor(num) - rounds down, ceil(num) - rounds up, sqrt(num)
"""

# USER INPUT
"""
fName = input("Enter your first name: ")
print("Hello",fName + "!")
"""

# LISTS (ARRAY)
"""
friends = ["Nil", 5, False, "shiv", "tuco"]
friends[1] = 10
print(friends[1])
print(friends[-1]) # returns first element from end
print(friends[0:3]) # returns range from 0 to 2
"""

# LIST FUNCTIONS
"""
luckyNumbers = [10,5,32,5,7,21]
names = ["Stanley", "Karen", "Jim", "Angela", "Pam"]
names.extend(luckyNumbers) # adds luckyNumbers to end of names list
names.append("Creed") # adds to end of list
names.insert(1, "Michael") # adds new element at specified index
names.remove("Creed")
names.clear() # removes all elements
names.pop() # removes last element
names.sort() # sorts by alphabetical order or smallest to biggest
names.reverse() # reverses the list
names2 = names.copy() # copies list into other variable
print(names.index("Kevin")) # returns index of an element
print(names.count("Jim")) # returns how many times element appears
"""

# TUPLES (CANT CHANGE THEM ONCE CREATED)
"""
coordinates = (4,5)
print(coordinates[1])
coordList = [(3,4), (3,6), (5,7)] # can add tuples in lists
print(coordList[1])
"""
