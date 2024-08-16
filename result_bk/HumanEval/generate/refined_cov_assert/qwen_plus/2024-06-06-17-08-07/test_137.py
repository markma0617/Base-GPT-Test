from code_137 import compare_one

def test():
    assert compare_one(1, 2.5) == 2.5
    assert compare_one(1, "2,3") == "2,3"
    assert compare_one("5,1", "6") == "6"
    assert compare_one("1", 1) == None
    assert compare_one(-1, "-1,5") == "-1,5"
    assert compare_one("1.0", 1) == None
    assert compare_one("3,14", 3.14) == "3,14"
    assert compare_one("1234", 1234) == None
    assert compare_one(0.1, "0,1") == 0.1
    assert compare_one("1.1", "1.2") == "1.2"
    assert compare_one("100,001", "100000.9") == "100,001"
