from code_117 import select_words

def test():
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]
    assert select_words("One two three four five", 2) == ["two", "three", "four"]
    assert select_words("No vowels here", 3) == ["here"]
    assert select_words("Consonant overload", 5) == ["overload"]
    assert select_words("", 1) == []
    assert select_words("Just testing", 6) == []
