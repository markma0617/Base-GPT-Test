from code_162 import string_to_md5
def test():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') is None
    assert string_to_md5('Python is awesome') == '522906b066c3ddc4c635b508f0c7c2b9'