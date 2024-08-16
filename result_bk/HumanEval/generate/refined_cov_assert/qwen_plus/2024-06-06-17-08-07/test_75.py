from code_75 import is_multiply_prime

def test():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(210) == True
    assert is_multiply_prime(330) == True
    assert is_multiply_prime(510) == True
    assert is_multiply_prime(770) == True
    assert is_multiply_prime(924) == True
    assert is_multiply_prime(8) == False
    assert is_multiply_prime(15) == False
    assert is_multiply_prime(20) == False
    assert is_multiply_prime(100) == False
