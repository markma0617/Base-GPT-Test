from code_64 import vowels_count

def test():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("strengthy") == 2
    assert vowels_count("puzzleY") == 2
    assert vowels_count("python") == 1
    assert vowels_count("Pythony") == 2
    assert vowels_count("algorithmY") == 4
    assert vowels_count("hello") == 2
    assert vowels_count("worldY") == 2
    assert vowels_count("programming") == 3
