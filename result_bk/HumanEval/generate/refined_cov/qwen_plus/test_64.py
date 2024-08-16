from code_64 import vowels_count

def test():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("hello") == 2
    assert vowels_count("Yosemite") == 3
    assert vowels_count("fly") == 1
