from code_162 import string_to_md5
def test():
    # Testing with a non-empty string
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    # Testing with an empty string
    assert string_to_md5('') is None

    # Testing with special characters
    assert string_to_md5('!@#%^&*()_+') == '5b905b7c361b0167f26d5084f7efae15'

    # Testing with numbers
    assert string_to_md5('1234567890') == 'e807f1fcf82d132f9bb018ca6738a19f'

    # Testing with uppercase and lowercase letters
    assert string_to_md5('Lorem Ipsum') == 'ae5f8ca037f7f0e3178d9f52eddb2d84'

    # Testing with a long string
    assert string_to_md5('a' * 1000) == '5c0bc9c8d5a0e152abe915e1cfaa5b92'

    # Testing with a mix of characters
    assert string_to_md5('abc123!@#') == 'c2282f5f8dcf3d2d32f7e6be2c5cb1a5'

    # Testing with whitespace
    assert string_to_md5('    ') == 'eccbc87e4b5ce2fe28308fd9f2a7baf3'

    # Testing with unicode characters
    assert string_to_md5('你好，世界') == 'cfcd208495d565ef66e7dff9f98764da'