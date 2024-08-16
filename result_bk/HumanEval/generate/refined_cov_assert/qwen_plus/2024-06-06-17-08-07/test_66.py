from code_66 import digitSum

def test():
    assert digitSum("") == 0
    assert digitSum("abAB") == 131
    assert digitSum("abcCd") == 67
    assert digitSum("helloE") == 69
    assert digitSum("woArBld") == 131
    assert digitSum("aAaaaXa") == 153
    assert digitSum("ALL_UPPER") == 305
    assert digitSum("all_lower") == 0
    assert digitSum("MiXeDcaSe") == 105
    assert digitSum("123UPPER") == 0
    assert digitSum("SINGLE_UPPERCASE_A") == 65
