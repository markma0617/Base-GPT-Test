from code_114 import minSubArraySum

def test():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([1, 2, 3, 4, 5, 6]) == 1
    assert minSubArraySum([-2, -3, 4, -1, -2, 1]) == -6
    assert minSubArraySum([-10, -20, -5, -3, -6]) == -44
