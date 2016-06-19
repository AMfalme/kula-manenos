# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import controller
import menu
import food

class  Test_menuTestCase(unittest.TestCase):
    
    def setUp(self):
        """Sets global variables"""
        
        self.food_name = "Food_name"
        self.price = 20
        self.value = "Carbs"
        self.pref = ""
        self.food_list = [self.food_name,self.price,self.value,self.pref]
        self._addition = menu.Menu(self.food_list)
        self._addition2 = food.Food(self.food_name,self.price,self.value,self.pref)
    
    def test_menu_object(self):
        """Tests if type of menu.Menu"""
        
        self.assertEqual(True, type(self._addition) is menu.Menu)
    
    def test_food_object(self):
        """Tests if type of food.Food"""
        
        self.assertEqual(True, type(self._addition2) is food.Food)
    
    def test_menu_instance(self):
        """Tests if is menu.Menu instance"""
        
        self.assertIsInstance(self._addition, menu.Menu)
        
    def test_food_instance(self):
        """Tests if is food.Food instance"""
        
        self.assertIsInstance(self._addition2, food.Food)
    
if __name__ == '__main__':
    unittest.main()