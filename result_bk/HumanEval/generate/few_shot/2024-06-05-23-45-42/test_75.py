from code_75 import is_multiply_prime

def test():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(15) == True
    assert is_multiply_prime(14) == False
    assert is_multiply_prime(7) == False
