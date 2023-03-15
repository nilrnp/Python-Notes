# FUNCTIONS
"""
def sayName(name, age = 5):
    print("Hi",name, ", you are " + str(age) + " years old!")
sayName("Nil", 21)
"""

# RETURN STATEMENTS
"""
def cube(side):
    return side*side*side
print(cube(5))
"""

# IF STATEMENTS
"""
isMale = True
isTall = False
if isMale and isTall: # and, or, not, >, <, >=, <=, ==, !=
    print("Both")
elif isTall:
    print("Only tall")
elif isMale:
    print("Only male")
else:
    print("Neither")
"""

# DICTIONARIES (key : value) (ALL KEYS MUST BE UNIQUE)
"""
monthConversion = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April"
}
print(monthConversion["Mar"])
print(monthConversion.get("Dec", "Not a valid key")) # get(key, default response if fail)
"""

# MATCH STATEMENTS
"""
age = 21
match age:
    case 12:
        print("12")
    case 18:
        print("18")
    case 21:
        print("21")
    case _:
        print("Default")
"""

# 2D LISTS
"""
numberGrid = [[3,4,5],[5,6,7],[7,8,9],[0]]
print(numberGrid[0][1])
print(numberGrid[3][0])
"""