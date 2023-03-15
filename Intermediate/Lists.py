# Lists (arrays)
# creating
myList = ["banana","cherry","apple"]
print(myList)

# can hold different types
myList2 = [5, 3, "apple", "orange"]
print(myList2)

# accessing values
item1 = myList[0]
secondLastItem = myList[-2] #reverse
print(secondLastItem)

# printing list
for item in myList2:
    print(item)

# checking if something in list
if "apple" in myList2:
    print("True")
else:
    print("False")

# getting length of list
print(len(myList2))

# common list functions
myList.append("bread")
myList.insert(2, "blueberry")
myList.remove("blueberry")
myList.pop() # removes from end

# sorting a list
numList = [1,2,3,5,2,1,2,3,1]
sortedList = sorted(numList)
print(sortedList)
numList.sort()
print(numList)

# slicing
a = numList[1:5] # index 1 to 4
b = numList[2:] # index 2 to end
c = numList[::-1] # reverses list

# copying a list
numList2 = numList # this points to same memory location, so any changes will affect both lists
numList3 = numList.copy()
numList4 = [i*i for i in numList] # makes list with square roots of numList