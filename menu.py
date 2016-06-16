class Menu(object):
    """class for modelling the structure and data of a menu
    """

    def __init__(self, foods):
        """create instance variable for array of foods
        """
        self.foods = foods

    def display(self):
        """return a nice readable format for the menu
        """
        out = "{0}\t\t\t{1}\n\n".format("name", "price")

        for food in self.foods:
            out += "{0}\t\t\t{1}\n".format(food.name, food.price)

        return out
