from code_38 import decode_cyclic
from code_38 import encode_cyclic
def test():
    assert encode_cyclic("abcdef") == "bcadef"
    assert encode_cyclic("abcde") == "cabde"
    assert encode_cyclic("abcdefgh") == "bcadefgh"
    assert encode_cyclic("a") == "a"
    assert decode_cyclic("bcadef") == "abcdef"
    assert decode_cyclic("cabde") == "abcde"
    assert decode_cyclic("bcadefgh") == "abcdefgh"
    assert decode_cyclic("a") == "a"