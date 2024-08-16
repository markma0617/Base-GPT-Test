from code_91 import is_bored

def test():
    assert is_bored("Hello world") == 0
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("I like dogs. I like cats too! I am happy.") == 3
    assert is_bored("I am bored? I am very bored.") == 2
