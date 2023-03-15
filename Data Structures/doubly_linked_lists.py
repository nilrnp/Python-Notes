
class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            return

        self.head = Node(data, self.head, None)


    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstring = ""
        while itr:
            llstring += str(itr.data) + " -> "
            itr = itr.next

        print(llstring)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        llstring = ""
        while itr:
            llstring += str(itr.data) + " -> "
            itr = itr.prev

        print(llstring)

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            previous_node = itr
            itr = itr.next
            itr.prev = previous_node


        itr.next = Node(data, None, itr)

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
                new_node = Node(value, itr.next, itr.prev)
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
    ll = Doubly_Linked_List()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()