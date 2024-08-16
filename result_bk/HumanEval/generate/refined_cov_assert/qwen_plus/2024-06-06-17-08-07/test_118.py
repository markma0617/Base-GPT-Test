from code_118 import get_closest_vowel

def test():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("consonant") == "o"
    assert get_closest_vowel("vowelEnd") == "e"
    assert get_closest_vowel("startVowel") == ""
    assert get_closest_vowel("NoVowel") == ""
    assert get_closest_vowel("vowelInMiddle") == "i"
    assert get_closest_vowel("AaEeIiOoUu") == "a"
