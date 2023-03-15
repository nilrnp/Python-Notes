# Dictionaries (Hash-maps)
# creating dictionaries
mydict = {"name": "John", "age": 28, "city": "New York"}
print(mydict)
mydict2 = dict(name="Mary", age = 28, city = "Los Angeles")
print(mydict2)

# printing keys
print(mydict["name"])

# removing entries
del mydict2["city"]
mydict.popitem()

# checking if something in dictionary
if "age" in mydict:
    print("true")

# looping through dictionary
for key in mydict2.keys():
    print(key)
for value in mydict.values():
    print(value)
for key, value in mydict2.items():
    print(key, value)

# copying dictionaries
mydictCopy = mydict.copy()
mydictCopy2 = dict(mydict2)