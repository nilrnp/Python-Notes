# Itertools, tools to use for iterators (data types used in loops)
# product, will combine lists (x1,x2) and (y1,y2) = (x1,y1), (x1,y2), (x2,y1)...
from itertools import product
a = [1,2, 3]
b = [4,5,6]
prod = product(a,b, repeat = 1) # repeat repeats how many times the product will be stored in list
print(list(prod))

# permutations, combines each element of list with itself with a specified length
from itertools import permutations
perm = permutations(a,2) # number specifies how many values to combine with
print(list(perm))

# combinations, makes all possible combinations with a specified length, combinations_with_replacement will do self values
from itertools import combinations
c = [1,2,3,4]
comb = combinations(c,2)
print(list(comb))

# accumulate, makes iterator that returns accumulated sums by default or other mathematical operations
from itertools import accumulate
import operator
acc = accumulate(c, func = operator.sub)
print(list(acc))

# groupby, creates dictionary for function values, key function required or a lambda function
from itertools import groupby
def smallThan3(x):
    return x < 3
gb = groupby(c, key = smallThan3)
for key, value in gb:
    print(key,list(value))

# infinite iterators
from itertools import count, repeat
for i in count(10): # counts from specified number until a break
    print(i)
    if i == 15:
        break

for i in repeat(1, 5): # (what to repeat, how many times)
    print(i)

