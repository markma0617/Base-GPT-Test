from code_117 import select_words

def test():
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]
    assert select_words("", 3) == []
    assert select_words("aaaaaa", 2) == []
    assert select_words("vowel", 3) == []
    assert select_words("Consonant C", 2) == []
    assert select_words("AeIoU", 1) == ["AeIoU"]
