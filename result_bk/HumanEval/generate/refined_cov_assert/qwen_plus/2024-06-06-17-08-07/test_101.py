from code_101 import words_string

def test():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert words_string("No space or,comma here") == ["No", "space", "or", "comma", "here"]
    assert words_string(",only,commas,") == ["only"]
    assert words_string("  leading,trailing  spaces  ") == ["leading", "trailing", "spaces"]
    assert words_string("") == []
    assert words_string(" , , , commas, , , ") == ["commas"]
    assert words_string("  spaces only  ,  ,  ") == ["spaces", "only"]
    assert words_string("multiple, , , commas, , , here") == ["multiple", "commas", "here"]
    assert words_string("special!@#$%^&*()_+ characters") == ["special", "characters"]
