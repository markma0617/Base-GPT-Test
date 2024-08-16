from code_82 import prime_length
def test():   
    assert prime_length('Hello') == True
    assert prime_length('abcdcba') == True
    assert prime_length('kittens') == True
    assert prime_length('orange') == False