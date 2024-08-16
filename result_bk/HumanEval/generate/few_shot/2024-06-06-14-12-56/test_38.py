from code_38 import decode_cyclic
from code_38 import encode_cyclic

def test():   
    assert encode_cyclic("abcdefgh") == "bcadefgh"
    assert encode_cyclic("12345") == "23145"
    assert encode_cyclic("hello") == "lohel"
    assert encode_cyclic("a") == "a"
    assert encode_cyclic("") == ""
    assert decode_cyclic("bcadefgh") == "abcdefgh"
    assert decode_cyclic("23145") == "12345"
    assert decode_cyclic("lohel") == "hello"
    assert decode_cyclic("a") == "a"
    assert decode_cyclic("") == ""
