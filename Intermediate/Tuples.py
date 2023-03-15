# Tuples are lists that can't be changed once created
# making a tuple
myTuple = ("Max", 28, "Boston", 4, 4, 2)
print(myTuple)
myTuple2 = tuple(["Max",28,"Boston"])

# accessing specific tuple elements
item = myTuple[1]
print(item)

# iterating over tuple
for i in myTuple2:
    print(i)

# checking if something in tuple
if "Max" in myTuple2:
    print("yes")

# length of tuple
print(len(myTuple))

# count of element in tuple
print(myTuple.count(28))

# get index of element in tuple
print(myTuple.index(28))

# converting tuple to list
myList = list(myTuple)

# slicing tuples
a = myTuple[1:] # 1 to end
b = myTuple[::-1] # reverse tuple

# unpacking tuple
name, age, place = myTuple2
print(name, age, place)
i1, *i2, i3 = myTuple # *i2 stores everything inbetween i1 and i3 as a list
print(i1, i2, i3)