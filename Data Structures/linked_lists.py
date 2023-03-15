
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstring = ""
        while itr:
            llstring += str(itr.data) + " -> "
            itr = itr.next

        print(llstring)

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next

        return length

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Not a valid index")

        if index == 0:
            self.head = self.head.next
            return

        current_index = 0
        itr = self.head
        while itr:
            if current_index == index-1:
                itr.next = itr.next.next
                break

            current_index += 1
            itr = itr.next

    def insert_at(self,index,value):
        if index < 0 or index > self.get_length():
            raise Exception("Not a valid index")

        if index == 0:
            self.insert_at_beginning(value)
            return

        current_index = 0
        itr = self.head
        while itr:
            if current_index == index - 1:
                new_node = Node(value, itr.next)
                itr.next = new_node
                break

            itr = itr.next
            current_index += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        current_index = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(current_index+1,data_to_insert)
                break
            itr = itr.next
            current_index += 1

    def remove_by_value(self, data):
        if self.head is None:
            return

        current_index = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(current_index)
                break
            itr = itr.next
            current_index += 1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([31,21,3,53,12])
    ll.remove_at(2)
    ll.insert_at(2, 69)
    ll.insert_after_value(69, 42)
    ll.remove_by_value(42)
    ll.print_linked_list()
