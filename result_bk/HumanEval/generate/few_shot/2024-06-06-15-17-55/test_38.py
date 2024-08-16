from code_38 import decode_cyclic
from code_38 import encode_cyclic

def test():
    assert encode_cyclic("abcde") == "bcdea"
    assert encode_cyclic("abcdef") == "bcdefa"
    assert encode_cyclic("abcdefgh") == "bcdefgha"
    assert encode_cyclic("abcdefghi") == "bcdefghia"
    assert encode_cyclic("abc") == "bca"

    assert decode_cyclic("bcdea") == "abcde"
    assert decode_cyclic("bcdefa") == "abcdef"
    assert decode_cyclic("bcdefgha") == "abcdefgh"
    assert decode_cyclic("bcdefghia") == "abcdefghi"
    assert decode_cyclic("bca") == "abc"
