# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import controller
import menu
import food

class  Test_menuTestCase(unittest.TestCase):
    #def setUp(self):
    #    new_menu = self.menu.Menu("Foods")
    
    def setUp(self):
        food_name = "Food_name"
        price = 20
        value = "Carbs"
        pref = ""
        food_list = [food_name,price,value,pref]
        self._addition = menu.Menu(food_list)
        self._addition2 = food.Food(food_name,price,value,pref)
        
    def test_menu_instance(self):
        self.assertIsInstance(self._addition, menu.Menu)
        
    def test_food_instance(self):
        self.assertIsInstance(self._addition2, food.Food)
    
    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

if __name__ == '__main__':
    unittest.main()