from code_94 import skjkasdkd

import unittest

def test_skjkasdkd(self):
    self.assertEqual(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)
    self.assertEqual(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)
    self.assertEqual(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)
    self.assertEqual(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)
    self.assertEqual(skjkasdkd([0,81,12,3,1,21]), 3)
    self.assertEqual(skjkasdkd([0,8,1,2,1,7]), 7)

TestGenerated = type('TestGenerated', (unittest.TestCase,), {'test_skjkasdkd': test_skjkasdkd})
