from code_105 import by_length

def test():
    assert by_length([]) == []
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    assert by_length([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    assert by_length([1, -1, 55]) == ["One"]
    assert by_length([1, 2, 10, 4, 5, 8, 2, 3]) == ["Two", "Two", "One", "Four", "Five", "Eight"]
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    assert by_length([5, 4, 3, 2, 1, -2, 0, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two"]
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, -1]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
