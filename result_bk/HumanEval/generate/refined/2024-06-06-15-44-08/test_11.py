from code_11 import string_xor

def test():   
    assert string_xor('010', '110') == '100'
    assert string_xor('10101', '11011') == '01110'
    assert string_xor('111', '111') == '000'
