from code_148 import bf

import unittest
from your_script import bf

class TestBfFunction(unittest.TestCase):

    def test_planets_between_given_planets(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))

    def test_planets_between_given_planets2(self):
        self.assertEqual(bf("Earth", "Mercury"), ("Venus"))

    def test_planets_between_given_planets3(self):
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_invalid_planets(self):
        self.assertEqual(bf("InvalidPlanet", "Neptune"), ())

    def test_same_planet(self):
        self.assertEqual(bf("Mars", "Mars"), ())

if __name__ == '__main__':
    unittest.main()
