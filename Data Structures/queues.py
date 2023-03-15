from collections import deque

# queue class implementation
class Queue:

    def __init__(self):
        self.container = deque()

    def enqueue(self,value):
        self.container.appendleft(value)

    def dequeue(self):
        return self.container.pop()

    def if_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# FIFO
if __name__ == '__main__':
    # Using List
    """
    stock_price_queue = []
    stock_price_queue.insert(0, 120) # insert at 0 position
    stock_price_queue.insert(0, 130)
    stock_price_queue.insert(0,140)
    print(stock_price_queue.pop()) # pop to remove first element that was put in
    """

    # Using deque
    """
    numbers_queue = deque()
    numbers_queue.appendleft(0) # appendleft to add at beginning of queue
    numbers_queue.appendleft(1)
    numbers_queue.appendleft(2)
    print(numbers_queue.pop())
    """

    # Queue Exercises
