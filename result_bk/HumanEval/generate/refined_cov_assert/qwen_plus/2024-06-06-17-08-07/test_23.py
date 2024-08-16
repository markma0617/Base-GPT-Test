from code_23 import strlen
def test(): 
    assert strlen("") == 0
    assert strlen("abc") == 3
    assert strlen("Hello, World!") == 13
    assert strlen("1234567890") == 10
    assert strlen("Python Unit Testing") == 16
    assert strlen("a" * 100) == 100
    assert strlen(" " * 10) == 10
    assert strlen("\t\n\r") == 3
    assert strlen("WITH Spaces") == 10
    assert strlen("1" + "2" * 999) == 1000