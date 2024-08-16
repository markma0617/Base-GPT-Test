from code_64 import vowels_count

def test():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("xyz") == 0
    assert vowels_count("test") == 1
    assert vowels_count("python") == 1
