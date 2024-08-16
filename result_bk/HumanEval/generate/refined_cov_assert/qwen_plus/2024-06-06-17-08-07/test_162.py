from code_162 import string_to_md5

def test():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') == None
    assert string_to_md5('Python') == 'b6dd2865b6d6ba33e0dd19189da93eb7'
    assert string_to_md5('Unit Test') == '0a721c0ef0270c7f402769735908d0b0'
    assert string_to_md5('This is a test') == '7d49c2f7b05258a7af7bc3c72b0be268'
    assert string_to_md5('Empty') == None
    assert string_to_md5('1234567890') == 'b0baee7474c7d8c4c2a746039869b8b2'
    assert string_to_md5('abcdefghijklmnopqrstuvwxyz') == 'd033e22ae348aeb5660fc2140aec3585'
    assert string_to_md5(' ') == 'e3b0c44298fc1c149afbf4c8996fb924'
    assert string_to_md5('!@#$%^&*()') == '098f6bcd4621d373cade4e832627b4f6'
