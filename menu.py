from food import Food 

class Menu(object):
	def __init__(self,foods):
		self.foods=foods

	def display(self):
		header = "{0}\t\t\t{1}\n".format("name", "price")
		print(header)
		for food in self.foods:
			print "{0}\t\t\t{1}".format(food.name, food.price)
			
