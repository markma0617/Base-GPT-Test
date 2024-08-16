from code_41 import car_race_collision

import unittest

def test():
    class TestCarRaceCollision(unittest.TestCase):
        
        def test_collision_zero(self):
            self.assertEqual(car_race_collision(0), 0)
        
        def test_collision_positive(self):
            self.assertEqual(car_race_collision(5), 25)
        
        def test_collision_negative(self):
            self.assertEqual(car_race_collision(-3), 9)
        
        def test_collision_large(self):
            self.assertEqual(car_race_collision(1000), 1000000)
    
    return TestCarRaceCollision
