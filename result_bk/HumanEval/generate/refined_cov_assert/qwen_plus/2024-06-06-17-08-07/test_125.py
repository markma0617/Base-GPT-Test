from code_125 import split_words

def test():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello,world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3
    assert split_words("NoSpaces,NoCommas") == 7
    assert split_words("A,B,C,D,E,F,G") == ["A", "B", "C", "D", "E", "F", "G"]
    assert split_words("alllowercase") == 3
    assert split_words("MixedCase,With,Commas") == ["MixedCase", "With", "Commas"]
    assert split_words("123456") == 3
    assert split_words("NoSpacesNoCommasButUppercase") == 5
    assert split_words("ab,cd,ef,gh") == ["ab", "cd", "ef", "gh"]
