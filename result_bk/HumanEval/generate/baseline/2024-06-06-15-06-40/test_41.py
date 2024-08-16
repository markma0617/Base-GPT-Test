from code_41 import car_race_collision

import unittest

def test():
    class TestCarRaceCollision(unittest.TestCase):
        
        def test_no_collision(self):
            self.assertEqual(car_race_collision(0), 0)
            
        def test_one_collision(self):
            self.assertEqual(car_race_collision(1), 1)
            
        def test_multiple_collisions(self):
            self.assertEqual(car_race_collision(2), 4)
            self.assertEqual(car_race_collision(3), 9)
            self.assertEqual(car_race_collision(5), 25)
            
    return TestCarRaceCollision
