from code_38 import decode_cyclic
from code_38 import encode_cyclic

def test():
    assert encode_cyclic("abcdef") == "bcdefa"
    assert encode_cyclic("abc") == "bca"
    assert encode_cyclic("123456789") == "234567891"
    assert encode_cyclic("pythonunittest") == "ythponnittestu"
    assert decode_cyclic("bcdefa") == "abcdef"
    assert decode_cyclic("bca") == "abc"
    assert decode_cyclic("234567891") == "123456789"
    assert decode_cyclic("ythponnittestu") == "pythonunittest"
    assert decode_cyclic(encode_cyclic("abcdef")) == "abcdef"
    assert decode_cyclic(encode_cyclic("pythonunittest")) == "pythonunittest"
