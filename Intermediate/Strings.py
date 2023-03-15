# Strings
# creating strings
myString1 = 'hello'
myString2 = "world"
longString = """
a
b
c
"""

# accessing characters
c1 = myString2[3]
substring = myString2[1:3]
reversedString = myString1[::-1]
everyOtherLetter = myString2[::2]

# concatenating
fullString = myString1 + " " + myString2

# printing every character in string
for x in fullString:
    print(x)

# seeing if letter in string
if 'e' in myString1:
    print("yes")

# removing extra space from string
wideString = "    hi     "
notWideString = wideString.strip()

# changing string to upper/lower case
myStringUpper = myString1.upper()
myStringLower = myString1.lower()

# other string functions
print(myString1.startswith('h')) # checks if string starts with a certain character
print(myString1.endswith('o')) # checks if string ends with a certain character
print(myString1.find('o')) # returns index where character is at
print(myString1.replace("hello", "goodbye")) # returns string with word replaced
print(myString1.count('o')) # returns how many characters are in string
splitString = fullString.split(" ") # returns string separated into a list based on the delimiter (default is a space)

# format strings
var = "Tom"
var2 = 38.12456
myString3 = "the variable is %s" % var # % in string is a placeholder, %s:string, %d:int, %f:float
print(myString3)
myString4 = "the variables are {} and {}".format(var,var2)
print(myString4)
myString5 = f"the variables are {var} and {var2*2}"
print(myString5)