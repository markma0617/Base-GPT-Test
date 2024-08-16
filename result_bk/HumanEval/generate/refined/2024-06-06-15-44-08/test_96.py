from code_96 import count_up_to

def test():   
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(0) == []
