import unittest
from employee import Employee

class newEmployee(unittest.TestCase):

    def setUp(self):
        self.David = Employee("David", "Beckham", 250)
    
    def test_give_default_raises(self):
        self.David.give_raise()
        self.assertEqual(self.David.annual_salary, 5250)

    def test_give_custom_raises(self):
        self.David.give_raise(100)
        self.assertEqual(self.David.annual_salary, 350)
    
if __name__ == '__main__':
    unittest.main()
