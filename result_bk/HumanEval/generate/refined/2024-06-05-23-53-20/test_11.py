from code_11 import string_xor
def test():
    assert string_xor('010', '110') == '100'
    assert string_xor('1010', '1111') == '0101'
    assert string_xor('000', '111') == '111'