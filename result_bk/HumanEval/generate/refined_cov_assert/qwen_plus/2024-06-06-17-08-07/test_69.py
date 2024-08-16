from code_69 import search

def test():
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([1, 1, 1, 2, 2, 3]) == 1
    assert search([6, 6, 6, 6, 6, 5, 5, 5]) == 6
    assert search([1, 2, 3, 4, 5, 5, 5]) == 5
    assert search([1, 1, 2, 2, 2, 3, 3, 3]) == 3
    assert search([10, 10, 9, 9, 9, 8, 8, 8, 8]) == 8
    assert search([100, 100, 100, 99, 99, 99, 99]) == 100
    assert search([1, 2, 3, 4, 5, 5, 5, 5]) == 5
