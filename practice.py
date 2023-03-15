
class Node:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class LL:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            return

        self.head = Node(value, self.head, None)

    def add_at_end(self,value):
        if self.head is None:
            self.add_at_beginning(value)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value,None,itr)

    def print_forwards(self):
        itr = self.head
        string = ""
        while itr:
            string += str(itr.value) + ' -> '
            itr = itr.next
        print(string)

    def print_backwards(self):
        itr = self.head
        string = ""
        while itr.next:
            itr = itr.next

        while itr:
            string += str(itr.value) + ' -> '
            itr = itr.prev
        print(string)

    def add_from_list(self, list):
        for i in list:
            self.add_at_end(i)

if __name__ == '__main__':
    linkedList = LL()
    linkedList.add_from_list([1,2,3,4,5,6,7,8,9])
    linkedList.print_forwards()
    linkedList.print_backwards()