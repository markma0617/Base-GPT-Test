from code_162 import string_to_md5

def test():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') == None
    assert string_to_md5('Python Testing') == 'b0baee9d679d0b22015138cc25008407'
