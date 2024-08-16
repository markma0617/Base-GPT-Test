from code_11 import string_xor
def test():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '101') == '010'
    assert string_xor('000', '111') == '111'
    assert string_xor('101', '101') == '000'
    assert string_xor('010', '010') == '000'