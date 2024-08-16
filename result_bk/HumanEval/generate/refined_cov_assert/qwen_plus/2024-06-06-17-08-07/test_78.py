from code_78 import hex_key

def test():
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2
    assert hex_key("AABBCCDD") == 0
    assert hex_key("1F") == 1
    assert hex_key("B3D5") == 3
    assert hex_key("") == 0
    assert hex_key("E000") == 0
