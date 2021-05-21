import unittest
from city_functions import get_formatted_name

class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        info= get_formatted_name('santiago', 'chile', 5000000)
        self.assertEqual(info, 'Santiago, Chile - population 5000000')

    def test_city_country_population(self):
        info= get_formatted_name('santiago', 'chile', 5000000)
        self.assertEqual(info, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
