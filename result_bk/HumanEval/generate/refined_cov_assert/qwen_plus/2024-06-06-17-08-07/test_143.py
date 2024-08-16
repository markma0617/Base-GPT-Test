from code_143 import words_in_sentence

def test():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("Python programming is fun") == "is"
    assert words_in_sentence("One two three four five") == "two three"
    assert words_in_sentence("Prime numbers are cool") == "numbers are"
    assert words_in_sentence("Keep coding everyday") == "coding"
    assert words_in_sentence("Simple sentences work") == "sentences work"
    assert words_in_sentence("Short words are best") == "are best"
    assert words_in_sentence("Eleven is a prime") == "Eleven is"
    assert words_in_sentence("Thirty seven is too") == "Thirty seven"
