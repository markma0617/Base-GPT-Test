from code_91 import is_bored
def test():
    assert is_bored("Hello world") == 0
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("I am happy. I feel alive! I am bored. I need a vacation.") == 2
    assert is_bored("I like coding. I solve problems. I create. I am excited!") == 4
    assert is_bored("I am here? I am there. I am everywhere!") == 3
    assert is_bored("I, me, myself. I like myself. I am special.") == 2
    assert is_bored("I am. I think? I see!") == 3
    assert is_bored("I wonder. I wander. I wish!") == 3
    assert is_bored("I am feeling good. I am feeling great!") == 2
    assert is_bored("I eat. I sleep. I repeat.") == 3