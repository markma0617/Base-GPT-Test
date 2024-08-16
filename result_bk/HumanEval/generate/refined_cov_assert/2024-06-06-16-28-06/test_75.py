from code_75 import is_multiply_prime

def test():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(60) == True
    assert is_multiply_prime(90) == True
    assert is_multiply_prime(31) == False
    assert is_multiply_prime(57) == False
    assert is_multiply_prime(27) == False
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(63) == True
    assert is_multiply_prime(13) == False
    assert is_multiply_prime(97) == False
