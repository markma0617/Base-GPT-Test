from code_91 import is_bored

def test():
    assert is_bored("Hello world") == 0
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("I am bored. I need a break!") == 2
    assert is_bored("I like to eat. Apples are my favorite fruit. I enjoy cooking.") == 2
