from code_50 import decode_shift
from code_50 import encode_shift

def test():
    assert encode_shift("hello") == "mjqqt"
    assert decode_shift("mjqqt") == "hello"
    assert encode_shift("Python") == "Rozuxu"
    assert decode_shift("Rozuxu") == "Python"
    assert encode_shift("shifted") == "ymxkxh"
    assert decode_shift("ymxkxh") == "shifted"
