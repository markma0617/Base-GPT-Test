from code_50 import decode_shift
from code_50 import encode_shift

def test():
    assert encode_shift("abc") == "fgh"
    assert encode_shift("xyz") == "cde"
    assert encode_shift("hello") == "mjqqt"
    
    assert decode_shift("fgh") == "abc"
    assert decode_shift("cde") == "xyz"
    assert decode_shift("mjqqt") == "hello"
