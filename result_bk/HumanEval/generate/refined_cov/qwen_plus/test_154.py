from code_154 import cycpattern_check

def test():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True
    assert cycpattern_check("xyzz", "yz") == True
    assert cycpattern_check("aaaa", "aaa") == True
    assert cycpattern_check("abcde", "xyz") == False
