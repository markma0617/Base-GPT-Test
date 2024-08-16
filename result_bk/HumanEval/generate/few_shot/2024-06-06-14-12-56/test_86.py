from code_86 import anti_shuffle

def test():
    assert anti_shuffle('Hi') == 'Hi'
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('Python Unit Test') == 'Phnoty Tinn Tetu'
    assert anti_shuffle('Quick Brown Fox') == 'Cikqu Bnoro Fox'
