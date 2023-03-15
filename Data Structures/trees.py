class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, type):
        prefix = ' ' * self.get_level() * 4

        if type == "name":
            print(prefix + "|__" + self.name)
            if len(self.children) > 0:
                for child in self.children:
                    child.print_tree("name")
        elif type == "designation":
            print(prefix + "|__" + self.designation)
            if len(self.children) > 0:
                for child in self.children:
                    child.print_tree("designation")
        elif type == "both":
            print(prefix + "|__" + self.name + "(" +self.designation + ")")
            if len(self.children) > 0:
                for child in self.children:
                    child.print_tree("both")

class LocationTree:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        prefix = ' ' * self.get_level() * 4

        print(prefix + "|__" + self.name)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

"""
def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Apple"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Toshiba"))

    phone = TreeNode("Phone")
    phone.add_child(TreeNode("Apple"))
    phone.add_child(TreeNode("Samsung"))
    phone.add_child(TreeNode("Google"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Hisense"))
    tv.add_child(TreeNode("TCL"))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    return root
"""

def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

def build_location_tree():
    gujarat_head = LocationTree("Gujarat")
    gujarat_head.add_child(LocationTree("Ahmedabad"))
    gujarat_head.add_child(LocationTree("Baroda"))

    karnataka_head = LocationTree("Karnataka")
    karnataka_head.add_child(LocationTree("Bangluru"))
    karnataka_head.add_child(LocationTree("Mysore"))

    jersey_head = LocationTree("New Jersey")
    jersey_head.add_child(LocationTree("Princeton"))
    jersey_head.add_child(LocationTree("Trenton"))

    cali_head = LocationTree("California")
    cali_head.add_child(LocationTree("San Francisco"))
    cali_head.add_child(LocationTree("Mountain View"))
    cali_head.add_child(LocationTree("Palo Alto"))

    india_head = LocationTree("India")
    india_head.add_child(gujarat_head)
    india_head.add_child(karnataka_head)

    us_head = LocationTree("USA")
    us_head.add_child(jersey_head)
    us_head.add_child(cali_head)

    global_head = LocationTree("Global")
    global_head.add_child(india_head)
    global_head.add_child(us_head)

    return global_head

if __name__ == '__main__':

    """
    tree = build_product_tree()
    tree.print_tree()
    """

    # Exercise 1
    # Extend tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class.
    # Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.
    root_node = build_management_tree()
    root_node.print_tree("name")
    print()
    root_node.print_tree("designation")
    print()
    root_node.print_tree("both")

    # Exercise 2
    root_node2 = build_location_tree()
    root_node2.print_tree()


