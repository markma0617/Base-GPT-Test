from code_11 import string_xor
def test():   
    assert string_xor('000', '000') == '000'
    assert string_xor('010', '110') == '100'
    assert string_xor('101', '111') == '010'