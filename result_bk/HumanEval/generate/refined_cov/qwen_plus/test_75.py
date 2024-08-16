from code_75 import is_multiply_prime

def test():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(84) == True
    assert is_multiply_prime(77) == True
    assert is_multiply_prime(100) == False
    assert is_multiply_prime(12) == False
