from code_41 import car_race_collision

import unittest

def test():
    class TestCarRaceCollision(unittest.TestCase):
        
        def test_collision_with_0_cars(self):
            self.assertEqual(car_race_collision(0), 0)
        
        def test_collision_with_1_car(self):
            self.assertEqual(car_race_collision(1), 1)
        
        def test_collision_with_2_cars(self):
            self.assertEqual(car_race_collision(2), 4)
        
        def test_collision_with_negative_cars(self):
            self.assertEqual(car_race_collision(-3), 9)
    
    return TestCarRaceCollision
