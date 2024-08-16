from code_11 import xor
from code_11 import string_xor

def test():   
    assert string_xor('010', '110') == '100'
    assert string_xor('101', '011') == '110'
    assert string_xor('1111', '0000') == '1111'
