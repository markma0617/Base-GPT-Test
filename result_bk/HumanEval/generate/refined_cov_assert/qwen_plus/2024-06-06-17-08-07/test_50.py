from code_50 import decode_shift
from code_50 import encode_shift

def test():
    assert encode_shift("hello") == "mjqqt"
    assert encode_shift("world") == "yrtln"
    assert decode_shift("mjqqt") == "hello"
    assert decode_shift("yrtln") == "world"
    assert encode_shift("abcdefg") == "fghijkl"
    assert decode_shift("fghijkl") == "abcdefg"
    assert encode_shift("xyz") == "abc"
    assert decode_shift("abc") == "xyz"
    assert encode_shift("abcdefghijklmnopqrstuvwxyz") == "fgijklmnopqrstuvwxyzabcde"
    assert decode_shift("fgijklmnopqrstuvwxyzabcde") == "abcdefghijklmnopqrstuvwxyz"
    assert decode_shift(encode_shift("special characters!")) == "special characters!"
