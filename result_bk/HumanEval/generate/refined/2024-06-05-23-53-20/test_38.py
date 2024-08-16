from code_38 import encode_cyclic

def test():
    assert encode_cyclic("abc") == "bca"
    assert encode_cyclic("abcdef") == "bcdefa"
    assert encode_cyclic("pythonunittest") == "ythontunitsest"
