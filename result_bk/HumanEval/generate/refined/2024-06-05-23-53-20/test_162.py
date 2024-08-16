from code_162 import string_to_md5
def test():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') == None
    assert string_to_md5('Python is great!') == 'e91f6f7bead9ee1a0a27b3d60f92c3a9'