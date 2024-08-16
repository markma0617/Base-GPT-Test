from code_109 import move_one_ball

import unittest

def move_one_ball(arr):
    if len(arr)==0:
        return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=arr.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
        if my_arr[i]!=sorted_array[i]:
            return False
    return True

class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(move_one_ball([]))

    def test_sorted_array(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_move_one_ball_true(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_move_one_ball_false(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))

if __name__ == '__main__':
    unittest.main()
