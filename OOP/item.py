import csv

class Item:
    # Class Attributes
    pay_rate = 0.8
    items_list = []

    # Constructor
    def __init__(self, name: str, price: float, quantity=0):
        # Validations
        assert price >= 0, "Price is not greater than or equal to 0"
        assert quantity >= 0, "Quantity is not greater than or equal to 0"

        # Set instance attributes
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Adding to items list
        Item.items_list.append(self)

    # property makes an attribute read-only (get), can't edit
    @property
    def name(self):
        return self.__name

    # setter allows attribute to be changed
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The item name is too long")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def applyDiscount(self):
        print(Item.pay_rate)
        self.__price = self.__price * Item.pay_rate

    def applyIncrement(self, value):
        self.__price = self.__price + self.__price * value

    def calculateTotalPrice(self):
        return self.__price * self.quantity

    def __connectToServer(self, server):
        pass

    def __prepareBody(self):
        return f"Hello Someone. \nWe have {self.name} {self.quantity} times."

    def __send(self):
        pass

    def sendEmail(self, server):
        self.__connectToServer(server)
        print(self.__prepareBody())
        self.__send()







    # class methods pass the object reference as the first argument, should be used when manipulating data
    @classmethod
    def instantiateFromCSV(cls):
        # reading from csv file
        with open('items.csv', 'r') as f:
            # converting csv items into a dictionary
            reader = csv.DictReader(f)
            # converting dictionary to a list
            items = list(reader)

        for item in items:
            Item(name = item.get('name'),price = float(item.get('price')), quantity = int(item.get('quantity')))

    # static methods are used when something does not have to be unique per instance
    @staticmethod
    def isInteger(num):
        # checks to see the num type
        if isinstance(num, float):
            # returns true if float has .0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Represents a class's objects as a string
    def __repr__(self):
        # Formatted String: f"TEXT"
        # self.__class__.__name__ gets name of class which object was created from
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"