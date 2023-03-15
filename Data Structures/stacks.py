from collections import deque

# Building a stack class
class Stack:

    def __init__(self):
        self.container = deque()

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def if_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


# LIFO
if __name__ == '__main__':
    # List as stack
    """
    s = []
    s.append(1) # append to insert at end
    s.append(2)
    s.append(3)
    s.append(4)
    print(s.pop()) # pop to remove from end
    print(s[-1]) # use -1 to get last element
    print(s)
    """

    # Deque as stack
    """
    stack = deque()
    stack.append(0)
    stack.append(1)
    stack.append(2)
    stack.pop()
    print(stack)
    """

    # Practice Problems
    # Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
    # reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
    string = "We will conquere COVID-19"
    string_arr = list(string)
    print(string_arr)
    reversed_string = ""
    for char in range(len(string_arr)):
        reversed_string += string_arr.pop()
    print(reversed_string)

    # Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses
    # are "{}',"()" or "[]". Use Stack class from the tutorial.
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))