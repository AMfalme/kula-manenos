from food import Food
from user import Users
from menu import Menu
from datetime import datetime


def createFoods():
    """create hardcoded food items and add them to an
    arrray then return the array
    """
    chapo = Food("Chapo", 10.00, "Carbohydrate", ["Vegeterian", "Vegan"])
    beans = Food("Beans", 20.00, "Protein", ["Vegeterian", "Vegan"])
    egg = Food("Egg", 10.00, "Protein", ["Vegeterian"])
    chips = Food("Chips", 70.00, "Carbohydrate", ["Vegeterian", "Vegan"])
    chicken = Food("Chicken", 125.00, "Protein", [])
    salad = Food("Salad", 100.00, "Vitamin", ["Vegeterian", "Vegan"])
    beef = Food("Beef", 100.00, "Protein", [])
    fish = Food("Fish", 130.00, "Protein", [])
    pork = Food("Pork", 150.00, "Protein", [])
    matoke = Food("Matoke", 70.00, "Carbohydrate", ["Vegeterian", "Vegan"])
    ugali = Food("Ugali", 40.00, "Carbohydrate", ["Vegeterian", "Vegan"])
    juice = Food("Juice", 70.00, "Vitamin", ["Vegeterian", "Vegan"])
    sukuma = Food("Sukuma", 20.00, "Vitamin", ["Vegeterian", "Vegan"])

    # create the array
    foods = [chapo, beans, egg, chips, chicken, salad,
             beef, fish, pork, matoke, ugali, juice, sukuma]

    return foods


def filteredMenu(pref):
    """takes a user's specified preference and then returns
    a menu with only those items
    """
    new = [food for food in createFoods() if pref in food.dietary_attributes]
    return Menu(new)


def main():
    """main controller function
    handles printing to std out, getting user input
    and instantiating needed classes"""
    # greet user and say time
    print ("\nHello\n")
    now = datetime.now().strftime('%H:%M')
    hour = int(now[:2])
    time_to_lunch = 12 - hour if hour <= 12 else 36 - hour
    print ("The time now is {0}, ~{1} hours to lunch.\n".format(
        now, time_to_lunch))

    # display nice-ish menu
    foods = createFoods()
    menu = Menu(foods)
    print ("Here is today's lunch menu\n\n{}\n\n".format("=" * 30))
    print (menu.display())

    # create a never ending input loop
    pref = raw_input("Enter 0 if Vegetarian or 1 if Vegan: ")
    print ("\nHere is your personalised menu.\n\n{}\n\n".format("=" * 30))
    print (filteredMenu("Vegan" if pref else "Vegetarian").display())


if __name__ == '__main__':
    main()
