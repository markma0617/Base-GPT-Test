from code_117 import select_words

def test():
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("simple white space", 2) == []
