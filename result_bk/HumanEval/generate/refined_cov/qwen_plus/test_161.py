from code_161 import solve

def test():
    assert solve("1234") == "4321"
    assert solve("ab") == "AB"
    assert solve("#a@C") == "#A@c"
    assert solve("1b2c3") == "3C2B1"
    assert solve("abcdefg") == "GFEEDCBA"
    assert solve("12!@#") == "!@#21"
