from code_86 import anti_shuffle
def test():
    assert anti_shuffle('Hi') == 'Hi'
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('Python Unit Test Case') == 'Phnoty Tni Ttse aCe'
    assert anti_shuffle('a b c d') == 'a b c d'
    assert anti_shuffle('123 321 456') == '123 123 456'
    assert anti_shuffle('abc def ghi') == 'abc def ghi'
    assert anti_shuffle('Hello, How are you?') == 'Hello, How aer you?'
    assert anti_shuffle('This is a test.') == 'This is a estt.'
    assert anti_shuffle('one two three') == 'eno owt eerht'