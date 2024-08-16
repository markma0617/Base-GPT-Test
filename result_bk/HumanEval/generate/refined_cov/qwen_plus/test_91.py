from code_91 import is_bored

def test():
    assert is_bored("Hello world") == 0
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("I am bored. Are you bored too? Yes, I am.") == 2
    assert is_bored("I wish it would rain. I hate sunny days.") == 2
    assert is_bored("We all feel bored sometimes.") == 0
