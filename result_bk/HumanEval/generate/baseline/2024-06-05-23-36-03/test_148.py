from code_148 import bf

import unittest

def test():
    
    class TestBF(unittest.TestCase):
        
        def test_example1(self):
            self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        
        def test_example2(self):
            self.assertEqual(bf("Earth", "Mercury"), ("Venus"))
        
        def test_example3(self):
            self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))
            
        def test_edge_case_same_planet(self):
            self.assertEqual(bf("Earth", "Earth"), ())
        
        def test_edge_case_invalid_planet(self):
            self.assertEqual(bf("Pluto", "Earth"), ())
    
    return TestBF
