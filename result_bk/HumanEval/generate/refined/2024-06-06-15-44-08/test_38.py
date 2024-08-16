from code_38 import decode_cyclic
from code_38 import encode_cyclic
def test():
    assert encode_cyclic("abcdefgh") == "bcadefgh"
    assert encode_cyclic("ijklmnopq") == "jklmnopqi"
    assert encode_cyclic("rstuvwxyz") == "stuvwxyzr"