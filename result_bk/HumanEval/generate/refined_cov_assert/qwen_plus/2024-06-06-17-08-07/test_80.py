from code_80 import is_happy

def test():
    assert is_happy('') == False
    assert is_happy('a') == False
    assert is_happy('aa') == False
    assert is_happy('abcd') == True
    assert is_happy('aabb') == False
    assert is_happy('adb') == True
    assert is_happy('xyy') == False
    assert is_happy('abcdd') == False
    assert is_happy('abcdefg') == True
    assert is_happy('abcba') == False
