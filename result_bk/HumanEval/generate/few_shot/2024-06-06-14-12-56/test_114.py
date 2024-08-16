from code_114 import minSubArraySum

def test():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([1, 2, 3, 4, 5]) == -15
    assert minSubArraySum([-5, -4, -3, -2, -1]) == -15
    assert minSubArraySum([5, 4, 3, 2, 1]) == -15
