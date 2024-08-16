from code_33 import sort_third

def test():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert sort_third([10, 11, 12, 13, 14, 15, 16]) == [10, 11, 12, 13, 14, 15, 16]
    assert sort_third([1, 2, 5, 4, 7, 6, 9]) == [1, 2, 5, 4, 7, 6, 9]
    assert sort_third([100, 200, 300, 400, 500, 600]) == [300, 200, 100, 400, 500, 600]
    assert sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [3, 2, 1, 4, 5, 6, 7, 8, 9]
    assert sort_third([10, 20, 30, 40, 50, 60, 70, 80, 90]) == [30, 20, 10, 40, 50, 60, 70, 80, 90]
    assert sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]
    assert sort_third([100, 200, 300, 400, 500, 600, 700, 800, 900]) == [300, 200, 100, 400, 500, 600, 700, 800, 900]
    assert sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11]
