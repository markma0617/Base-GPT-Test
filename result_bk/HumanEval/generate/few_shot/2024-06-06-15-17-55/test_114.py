from code_114 import minSubArraySum

def test():   
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([5, 7, -2, 3, 6, -1]) == -2
