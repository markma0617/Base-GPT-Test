from code_161 import solve

def test():
    assert solve("1234") == "4321"
    assert solve("ab") == "AB"
    assert solve("#a@C") == "#A@c"
    assert solve("tEstStrING") == "TeSTsTRing"
    assert solve("1234Ab") == "BA4321"
