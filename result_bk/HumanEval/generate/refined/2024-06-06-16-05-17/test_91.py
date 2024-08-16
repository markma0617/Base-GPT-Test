from code_91 import is_bored
def test():
    assert is_bored("Hello world") == 0
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("I am happy. I am sad. I am bored!") == 2