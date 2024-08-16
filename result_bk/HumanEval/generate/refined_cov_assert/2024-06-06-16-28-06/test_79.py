from code_79 import decimal_to_binary

def test():
    assert decimal_to_binary(0) == "db0db"
    assert decimal_to_binary(1) == "db1db"
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"
    assert decimal_to_binary(7) == "db111db"
    assert decimal_to_binary(8) == "db1000db"
    assert decimal_to_binary(63) == "db111111db"
    assert decimal_to_binary(127) == "db1111111db"
    assert decimal_to_binary(255) == "db11111111db"
    assert decimal_to_binary(1023) == "db1111111111db"
