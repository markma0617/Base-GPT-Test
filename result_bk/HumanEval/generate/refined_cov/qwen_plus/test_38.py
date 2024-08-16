from code_38 import decode_cyclic
from code_38 import encode_cyclic

def test():
    assert encode_cyclic("hello") == "elhlo"
    assert encode_cyclic("编码") == "码编"
    assert encode_cyclic("abc123") == "bc1a23"
    assert decode_cyclic("elhlo") == "hello"
    assert decode_cyclic("码编") == "编码"
    assert decode_cyclic("bc1a23") == "abc123"