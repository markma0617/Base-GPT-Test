from code_59 import largest_prime_factor

def test():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(2048) == 2
    assert largest_prime_factor(315) == 5
    assert largest_prime_factor(972) == 3
    assert largest_prime_factor(10000) == 2
    assert largest_prime_factor(123456789) == 3803
    assert largest_prime_factor(72) == 3
    assert largest_prime_factor(120) == 5
    assert largest_prime_factor(1001) == 7
    assert largest_prime_factor(10101) == 3
