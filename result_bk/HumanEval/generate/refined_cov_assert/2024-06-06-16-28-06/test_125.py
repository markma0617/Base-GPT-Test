from code_125 import split_words

def test():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello,world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3
    assert split_words("apple,orange,banana") == ["apple", "orange", "banana"]
    assert split_words("apple") == ["apple"]
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("12345") == 0
    assert split_words("a,b") == ["a", "b"]
    assert split_words("cat,dog") == ["cat", "dog"]
    assert split_words("Python is fun") == ["Python", "is", "fun"]
