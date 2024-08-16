from code_64 import vowels_count

def test():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("hello") == 2
    assert vowels_count("HELLO") == 2
    assert vowels_count("queue") == 2
    assert vowels_count("QUEUE") == 2
    assert vowels_count("fly") == 1
    assert vowels_count("FLY") == 1
    assert vowels_count("sky") == 2
    assert vowels_count("SKY") == 2
