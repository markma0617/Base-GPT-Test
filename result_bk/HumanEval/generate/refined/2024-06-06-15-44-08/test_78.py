from code_78 import hex_key

def test():
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
