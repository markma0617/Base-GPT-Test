from code_80 import is_happy

def test():
    assert is_happy("abcd") == True
    assert is_happy("aabb") == False
    assert is_happy("adb") == True
    assert is_happy("xyy") == False
    assert is_happy("abcde") == True
    assert is_happy("xxyy") == False
