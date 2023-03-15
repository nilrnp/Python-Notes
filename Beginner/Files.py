# READING FROM FILE
'''
employeeFile = open("employees.txt", "r") # r - read, w - writes to file but overrides entire file, a - append to end, + to do multiple

print(employeeFile.read()) # returns everything in file
print(employeeFile.readline()) # returns line by line in file
print(employeeFile.readable()) # returns whether there is stuff in file
print(employeeFile.readlines()) # puts each line in a tuple

for employee in employeeFile.readlines():
    print(employee)


employeeFile.close() # close file once we are done using it
'''

# APPENDING TO FILE
'''
employeeFile = open("employees.txt", "a")
employeeFile.write("\nToby - Human Resources")
employeeFile.close()
'''

# WRITING TO FILE
'''
employeeFile = open("employees.txt", "w")
employeeFile.write("\nToby - Human Resources")
employeeFile.close()
'''
