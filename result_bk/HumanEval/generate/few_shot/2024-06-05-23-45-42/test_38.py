from code_38 import encode_cyclic

def test():
    assert encode_cyclic("abc") == "bca"
    assert encode_cyclic("abcdefgh") == "bcaefghd"
    assert encode_cyclic("python") == "ythpon"
    assert decode_cyclic("bca") == "abc"
    assert decode_cyclic("bcaefghd") == "abcdefgh"
    assert decode_cyclic("ythpon") == "python"
