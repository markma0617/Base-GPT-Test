from code_137 import compare_one

def test():
    assert compare_one(1, 2.5) == 2.5
    assert compare_one(1, "2,3") == "2,3"
    assert compare_one("5,1", "6") == "6"
    assert compare_one("1", 1) == None
    assert compare_one(-1.5, "-1,5") == "-1,5"
    assert compare_one("4.2", 4) == "4.2"
    assert compare_one("10", 10.0) == 10.0
