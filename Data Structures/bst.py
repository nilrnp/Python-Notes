class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        # visit base node
        elements.append(self.data)

        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        # visit base node
        elements.append(self.data)

        return elements

    def search(self,value):
        if self.data == value:
            return True

        if value < self.data:
            # value might be in left subtree
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            # value might be in right subtree
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        values = self.in_order_traversal()
        return values[0]

    def find_max(self):
        values = self.in_order_traversal()
        return values.pop()

    def calculate_sum(self):
        values = self.in_order_traversal()
        sum = 0
        for i in range(len(values)):
            sum += values[i]
        return sum

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 5, 4, 23, 2, 45, 13, 4]
    numbersTree = build_tree(numbers)
    print(numbersTree.in_order_traversal())
    print(numbersTree.pre_order_traversal())
    print(numbersTree.post_order_traversal())
    print(numbersTree.search(23))
    print(numbersTree.find_min())
    print(numbersTree.find_max())
    print(numbersTree.calculate_sum())
