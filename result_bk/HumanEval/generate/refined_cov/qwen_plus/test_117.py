from code_117 import select_words

def test():
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]
    assert select_words("", 1) == []
    assert select_words("AbCdeFgHiJ", 5) == ["Cde", "Fg"]
    assert select_words("ConsonantChallenge", 7) == ["Challenge"]
