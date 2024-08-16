from code_84 import solve

def test():
    assert solve(0) == "0"
    assert solve(8) == "1000"
    assert solve(13) == "1101"
    assert solve(789) == "1100010101"
    assert solve(10000) == "10011100010000"
    assert solve(1111) == "10001010111"
    assert solve(777) == "1100001001"
    assert solve(1) == "1"
    assert solve(10101) == "101101001111"
    assert solve(9999) == "10011100001111"
