# Exceptions and Errors

# error types
"""
print("hello")) # syntax error
c = 5 + "s" # type error
import sadasda # modulenotfound error
b = d # name error
f = open("somefile.txt") # filenotfound error
a = [1,2,3].remove(4) # value error
a[4] # index error
myDict = {"a":1,"b":2}.get("c") # key error
"""

# raising exceptions
"""
x = -3
if x < 0:
    raise Exception("x should be positive")

assert(x >= 0), "x should be positive"
"""

# try catch statements
try:
    a = 5/0
except Exception as e:
    print("error:", e)

try:
    b = 3/0
except ZeroDivisionError as e:
    print(e)
else:
    print("everything is fine")
finally: # will always run
    print("cleaning up...")