from code_91 import is_bored

def test():
    assert is_bored("Hello world") == 0
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("I am bored. Are you bored too?") == 1
    assert is_bored("I enjoy programming. However, sometimes I feel bored.") == 2
    assert is_bored("Let's go for a walk. I need some fresh air.") == 1
    assert is_bored("The dog chased the cat. I watched them play.") == 1
    assert is_bored("It's a beautiful day. I wish I could stay outside.") == 1
    assert is_bored("I, as a language model, can get bored sometimes. Can you relate?") == 2
    assert is_bored("We had a long day. I just want to relax now.") == 1
    assert is_bored("What did you do today? I spent the whole day coding.") == 1
