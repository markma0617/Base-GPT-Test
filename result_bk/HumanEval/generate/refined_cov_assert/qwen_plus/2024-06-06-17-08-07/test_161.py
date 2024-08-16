from code_161 import solve

def test():
    assert solve("1234") == "4321"
    assert solve("ab") == "AB"
    assert solve("#a@C") == "#A@c"
    assert solve("9B#9") == "9b#9"
    assert solve("hello") == "HELLO"
    assert solve("World!") == "wORLD!"
    assert solve("@$%^&*") == "@$%^&*"
    assert solve("") == ""
    assert solve("1a2b3c") == "3cb2a1"
    assert solve("9@8#7&6*5") == "5*&6#789"
