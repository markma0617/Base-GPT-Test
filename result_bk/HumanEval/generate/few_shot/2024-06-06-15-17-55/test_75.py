from code_75 import is_multiply_prime

def test():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(24) == True
    assert is_multiply_prime(20) == False
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(64) == False
