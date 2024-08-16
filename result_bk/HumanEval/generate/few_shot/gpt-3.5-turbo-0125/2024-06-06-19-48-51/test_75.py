from code_75 import is_multiply_prime

def test():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(27) == True
    assert is_multiply_prime(20) == False
    assert is_multiply_prime(24) == True
    assert is_multiply_prime(31) == False
