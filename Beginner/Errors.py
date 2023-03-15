try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Invalid Input")

