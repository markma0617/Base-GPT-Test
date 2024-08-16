from code_161 import solve

def test():
    assert solve("1234") == "4321"
    assert solve("ab") == "AB"
    assert solve("#a@C") == "#A@c"
    assert solve("hello") == "OLLEh"
    assert solve("123ABC") == "cba321"
    assert solve("##!@") == "@!##"
    assert solve("") == ""
    assert solve("a") == "A"
    assert solve("123") == "321"
    assert solve("aBcDeF") == "fEdCbA"
