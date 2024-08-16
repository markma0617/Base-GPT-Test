from code_125 import split_words
def test():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello,world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3
    assert split_words("Hello world,!") == ["Hello", "world,!"]
    assert split_words("Hello,Hello,world !") == ["Hello,Hello,world", "!"]