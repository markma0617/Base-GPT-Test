from code_125 import split_words
def test():   
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello,world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3 
    assert split_words("NoSpaces,NoCommas") == 0
    assert split_words("Test123") == 2
    assert split_words("all lowercase, no spaces") == ["all", "lowercase", "no", "spaces"]