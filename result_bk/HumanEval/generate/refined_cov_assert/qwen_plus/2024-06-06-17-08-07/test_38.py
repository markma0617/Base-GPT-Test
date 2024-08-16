from code_38 import decode_cyclic
from code_38 import encode_cyclic

def test():
    assert encode_cyclic("hello") == "elhlo"
    assert encode_cyclic("编码") == "码编"
    assert encode_cyclic("abcde") == "bcdea"
    assert encode_cyclic("编码测试") == "码测编码"
    assert encode_cyclic("12345678") == "23456781"
    assert encode_cyclic("abcdefg") == "bcdefga"
    assert encode_cyclic("编码测试123") == "码测123编码"
    assert decode_cyclic("elhlo") == "hello"
    assert decode_cyclic("码编") == "编码"
    assert decode_cyclic("bcdea") == "abcde"
    assert decode_cyclic("码测编码") == "编码测试"
    assert decode_cyclic("23456781") == "12345678"
    assert decode_cyclic("bcdefga") == "abcdefg"
    assert decode_cyclic("码测123编码") == "编码测试123"
