from code_64 import vowels_count

def test():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("Python") == 2
    assert vowels_count("qwrtY") == 1
    assert vowels_count("AEIOUY") == 6
