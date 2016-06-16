class Food(object):
    """models a food object"""

    def __init__(self, name, price, nutrition_value, *dietary_attributes):
        """constructor for a food item"""
        self.name = name
        self.price = price
        self.nutrition_value = self.nutrition_value
        self.dietary_attributes = []

        for attribute in dietary_attributes:
            self.dietary_attributes.append(attribute)
