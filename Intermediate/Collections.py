# Collections
# counter, stores elements as dictionary keys, and counts as dictionary values
"""
from collections import Counter
a = "aaabbbccccd"
myCounter = Counter(a)
print(myCounter)
print(myCounter.values())
print(myCounter.items())
print(myCounter.most_common(2)) # will print 2 most common elements
"""

# named tuple, like a struct
"""
from collections import namedtuple
Point = namedtuple('Point','x,y') # will make class called point, with fields x and y
pt = Point(3,4)
print(pt.x, pt.y)
"""

# ordered dict, dictionary that remembers order in which items are inserted (kinda useless now)
"""
from collections import OrderedDict
oDict = OrderedDict()
oDict['a'] = 1
oDict['b'] = 3
print(oDict)
"""

# default dict, dictionary that will have a default value for keys that haven't been set
"""
from collections import defaultdict
dDict = defaultdict(int) # need to specify type of default value
dDict['a'] = 1
dDict['b'] # will default value to 0
print(dDict)
"""

# deque, double ended queue
"""
from collections import deque
myDeq = deque()
myDeq.append(3)
myDeq.appendleft(2)
myDeq.popleft() # remove from beginning rather than end
"""

