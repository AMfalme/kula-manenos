# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import controller
import menu


class  Test_menuTestCase(unittest.TestCase):
    #def setUp(self):
    #    new_menu = self.menu.Menu("Foods")
    
    def setUp(self):
        self._addition = menu.Menu("Foood")
        
    def test_menu_instance(self):
        self.assertIsInstance(self._addition, menu.Menu)
        

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None


if __name__ == '__main__':
    unittest.main()

