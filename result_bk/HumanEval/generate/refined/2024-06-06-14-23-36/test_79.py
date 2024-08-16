from code_79 import decimal_to_binary
def test():
    assert decimal_to_binary(0) == "db0db"
    assert decimal_to_binary(1) == "db1db"
    assert decimal_to_binary(15) == "db1111db"