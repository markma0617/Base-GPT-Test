from code_66 import digitSum

def test():
    assert digitSum("") == 0
    assert digitSum("abAB") == 131
    assert digitSum("abcCd") == 67
    assert digitSum("helloE") == 69
    assert digitSum("woArBld") == 131
    assert digitSum("aAaaaXa") == 153
    assert digitSum("ABBCCDDEEFF") == 585
    assert digitSum("qqqqqQQQQQQQ") == 546
    assert digitSum("AAaaBBbbCCcc") == 330
    assert digitSum("ZzYyXxWwVvUu") == 631
