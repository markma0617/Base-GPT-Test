from code_143 import words_in_sentence

def test():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("a bb ccc dddd eeeee") == "a bb"
    assert words_in_sentence("one two three four five") == "one two"
    assert words_in_sentence("prime numbers are 2 3 5 7 11") == "are 2 3 5 7 11"
    assert words_in_sentence("python is a great language") == "is a"
    assert words_in_sentence("hello world") == "world"
    assert words_in_sentence("apple banana cherry date") == "apple date"
    assert words_in_sentence("try this out for size") == "try this for size"
    assert words_in_sentence("a quick brown fox jumps over lazy dog") == "a quick fox"
