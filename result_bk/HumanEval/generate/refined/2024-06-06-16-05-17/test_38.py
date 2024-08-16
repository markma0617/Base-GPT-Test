from code_38 import decode_cyclic
from code_38 import encode_cyclic

def test():
    assert encode_cyclic("abcdefghi") == "bcadefghi"
    assert encode_cyclic("abcd") == "badc"
    assert encode_cyclic("abcdefg") == "bcadefg"
