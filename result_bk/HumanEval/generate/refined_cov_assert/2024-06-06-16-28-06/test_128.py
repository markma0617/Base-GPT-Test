from code_128 import prod_signs
def test():   
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) == None
    assert prod_signs([0]) == 0
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([1, 2, 3, 4]) == 10
    assert prod_signs([-1, -2, 3, 4]) == 10
    assert prod_signs([0, 0, 0]) == 0
    assert prod_signs([1, -1, 1, -1]) == -4
    assert prod_signs([1, 2, -3, 0]) == -6