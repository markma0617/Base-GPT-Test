from code_79 import decimal_to_binary

def test():
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"
    assert decimal_to_binary(0) == "db0db"
    assert decimal_to_binary(127) == "db1111111db"
    assert decimal_to_binary(255) == "db11111111db"
    assert decimal_to_binary(1024) == "db100000000db"
    assert decimal_to_binary(0o777) == "db1111111db"
    assert decimal_to_binary(0b101010) == "db101010db"
    assert decimal_to_binary(-1) == "db-1db"
    assert decimal_to_binary(4294967295) == "db111111111111111111111111111111db"
