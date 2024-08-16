from code_151 import double_the_difference

def test():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([]) == 0
    assert double_the_difference([4, 5.5, 7, -3]) == 49
    assert double_the_difference([2.5, 3.7, 5]) == 0
    assert double_the_difference([1, -3, 9, 0.5]) == 1
    assert double_the_difference([6, 8, -9, 11.5]) == 121
    assert double_the_difference([101, -202, 303, -404.0]) == 101*101
