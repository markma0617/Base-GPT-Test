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
        
        def test_invalid_planet_names(self):
            self.assertEqual(bf("Pluto", "Neptune"), ())
            self.assertEqual(bf("Venus", "Pluto"), ())
            self.assertEqual(bf("Mars", "Mars"), ())
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBF)
    unittest.TextTestRunner(verbosity=2).run(suite)

test()
