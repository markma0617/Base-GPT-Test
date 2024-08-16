from code_151 import double_the_difference

def test():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([]) == 0
    assert double_the_difference([5.5, 7.3, -3.0]) == 0
    assert double_the_difference([-4, 6, 8, 9]) == 81
    assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 165
    assert double_the_difference([11, 12, 13, 14, 15]) == 455
    assert double_the_difference([-5, -6, -7, -8, -9]) == 0