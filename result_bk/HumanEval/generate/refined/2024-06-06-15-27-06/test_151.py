from code_151 import double_the_difference
def test():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([1.5, 3, 0.5]) == 10
    assert double_the_difference([]) == 0