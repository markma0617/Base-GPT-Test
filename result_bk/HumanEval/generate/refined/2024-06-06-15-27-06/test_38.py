from code_38 import decode_cyclic
from code_38 import encode_cyclic
def test():
    assert encode_cyclic("abcdef") == "defabc"
    assert encode_cyclic("xyz") == "yzx"
    assert encode_cyclic("123456789") == "456789123"
    assert decode_cyclic("defabc") == "abcdef"
    assert decode_cyclic("yzx") == "xyz"
    assert decode_cyclic("456789123") == "123456789"