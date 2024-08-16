from code_66 import digitSum

def test():
    assert digitSum("") == 0
    assert digitSum("abAB") == 131
    assert digitSum("abcCd") == 67
