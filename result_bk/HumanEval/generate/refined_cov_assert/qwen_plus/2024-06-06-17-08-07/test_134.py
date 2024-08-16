from code_134 import check_if_last_char_is_a_letter

def test():
    assert check_if_last_char_is_a_letter("apple pie") == False
    assert check_if_last_char_is_a_letter("apple pi e") == True
    assert check_if_last_char_is_a_letter("apple pi e ") == False
    assert check_if_last_char_is_a_letter("") == False
    assert check_if_last_char_is_a_letter("hello world") == False
    assert check_if_last_char_is_a_letter("hello worl d") == True
    assert check_if_last_char_is_a_letter("hello worl d ") == False
    assert check_if_last_char_is_a_letter("123abc") == False
    assert check_if_last_char_is_a_letter("123abc ") == False
    assert check_if_last_char_is_a_letter("a b c") == True
