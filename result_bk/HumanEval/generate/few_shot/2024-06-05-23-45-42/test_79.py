from code_79 import decimal_to_binary

def test():
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"
    assert decimal_to_binary(5) == "db101db"
    assert decimal_to_binary(11) == "db1011db"
    assert decimal_to_binary(0) == "db0db"
