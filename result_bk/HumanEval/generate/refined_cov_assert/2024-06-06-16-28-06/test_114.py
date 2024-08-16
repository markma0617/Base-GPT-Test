from code_114 import minSubArraySum

def test():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([1, 2, 3, 4, 5, 6]) == -21
    assert minSubArraySum([-1, -2, 3, -4, 5, -6]) == -9
    assert minSubArraySum([-2, -3, -1, -4, -5]) == -15
    assert minSubArraySum([1, -2, 3, -4, 5, -6]) == -4
    assert minSubArraySum([10, -12, 15, -20, 25, -30]) == -27
    assert minSubArraySum([100, -200, 300, -400, 500, -600]) == -600
    assert minSubArraySum([-10, -20, -30]) == -60
    assert minSubArraySum([10, 20, 30]) == -60
