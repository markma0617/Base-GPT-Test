from code_162 import string_to_md5
def test():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') == None
    assert string_to_md5('Python is awesome!') == 'c4d5d12c4f9989fae3c53df9a13ec48f'