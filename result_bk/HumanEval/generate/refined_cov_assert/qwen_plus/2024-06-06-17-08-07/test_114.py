from code_114 import minSubArraySum

def test():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([1, 2, 3, -4, 5, -6]) == -6
    assert minSubArraySum([1, -2, 3, -4, 5]) == -3
    assert minSubArraySum([-1, -2, -3, -4, -5]) == -15
    assert minSubArraySum([0, 1, -2, 3]) == -2
    assert minSubArraySum([5, 4, 3, 2, 1]) == 1
    assert minSubArraySum([1, 2, 3, 4, 5]) == 1
    assert minSubArraySum([-1, -2, -3, -4, -5, -6]) == -6
    assert minSubArraySum([1, -1, 1, -1]) == -1
