# Lists [0,1,2,3,4,...]
stock_price = [298,305,320,301,292]

# 2D Lists
stock_prices = [
    [32,34,13],
    [56,53,21,57]
]

# Exercise 1
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out
expenses = [2200,2350,2600,2130,2190]
# In Feb, how many dollars you spent extra compare to January?
print(expenses[1]-expenses[0])
# Find out your total expense in first quarter (first three months) of the year.
print(expenses[0]+expenses[1]+expenses[2])
# Find out if you spent exactly 2000 dollars in any month
print(2000 in expenses)
# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3] = expenses[3] - 200

# Exercise 2
#You have a list of your favourite marvel super heros
heros=['spider man','thor','hulk','iron man','captain america']
# Length of the list
print(len(heros))
# Add 'black panther' at the end of this list
heros.append('black panther')
# You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(3,'black panther')
# Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ['doctor strange']
# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

# Exercise 3
# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a
# user using input() function
max_number = int(input("Enter a max number: "))
odd_list = []
for i in range(1, max_number):
    if i % 2 != 0:
        odd_list.append(i)
print(odd_list)