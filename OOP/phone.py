from item import Item

# Inheritance from Item class
class Phone(Item):
    pay_rate = .75
    def __init__(self, name: str, price: float, quantity=0, brokenPhones = 0):
        # Calling parent constructor
        super().__init__(name,price,quantity)

        # Validations
        assert brokenPhones >= 0, f"Broken phones {brokenPhones} is not greater than or equal to 0"

        # Set instance attributes
        self.brokenPhones = brokenPhones
