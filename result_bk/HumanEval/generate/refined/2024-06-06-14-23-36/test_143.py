from code_143 import words_in_sentence

def test():   
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("coding is fun") == "is fun"
