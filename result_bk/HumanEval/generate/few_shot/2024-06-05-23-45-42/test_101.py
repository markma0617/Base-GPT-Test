from code_101 import words_string
def test():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert words_string("") == []
    assert words_string("Hello") == ["Hello"]
    assert words_string("How are you today?") == ["How", "are", "you", "today?"]