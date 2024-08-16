from code_96 import count_up_to

def test():
    assert count_up_to(0) == []
    assert count_up_to(1) == []
    assert count_up_to(2) == []
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]
    assert count_up_to(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert count_up_to(13) == [2, 3, 5, 7, 11]
    assert count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
