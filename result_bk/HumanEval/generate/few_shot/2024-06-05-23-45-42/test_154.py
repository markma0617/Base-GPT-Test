from code_154 import cycpattern_check

def test():   
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True
