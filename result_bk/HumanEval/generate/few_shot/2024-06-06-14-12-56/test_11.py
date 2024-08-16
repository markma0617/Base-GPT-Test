from code_11 import xor
from code_11 import string_xor
def test():
    assert string_xor('010', '110') == '100'
    assert string_xor('1010', '1001') == '0011'
    assert string_xor('1111', '1111') == '0000'
    assert string_xor('000', '111') == '111'