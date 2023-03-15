# Sets (unordered, mutable, no duplicates)
# creating a set
myset = {1,2,3,4,5,1} # only one 1 will be in set
print(myset)
myset2 = set("Hello")
print(myset2)
myset3 = set() # empty set

# adding/removing to/from set
myset3.add(2)
myset3.add(5)
myset3.add(7)
myset3.remove(2) # will remove element if its in set, if not in set it will cause error
myset3.discard(4) # will remove element if its in set, if not it will do nothing
myset.pop() # removes random element

# iterating over set
for i in myset3:
    print(i)

# checking if something in set
if 4 in myset3:
    print("true")

# comparisons
odd = {1,3,5,7,9}
even = {0,2,4,6,8}
primes = {2,3,5,7}

u = odd.update(even) # combines sets without duplication
i = odd.intersection(primes) # returns set of values that are in both sets
dif = odd.difference(primes) # returns set of values that in first set but not in second set
dif2 = even.symmetric_difference(primes) # returns set of values that are not duplicated in each set

# updating sets
odd.update(even) # updates first set with elements in the second set
odd.intersection_update(even) # updates first set with only elements in both sets
odd.difference_update(primes) # updates first set with only elements not in both sets
odd.symmetric_difference_update(even) # updates first set with elements not duplicated in each set

# super/sub sets
print(odd.issubset(primes)) # subset means all elements in first set are also in second set
print(odd.issuperset(primes)) # superset means all elements in first set are not in second set
print(odd.isdisjoint(primes)) # disjoint means all elements in first set are different from second set

# copying sets
oddCopy = odd.copy()
evenCopy = set(even)

# frozen set (cant be changed after being created)
frzSet = frozenset([1,2,3,4])