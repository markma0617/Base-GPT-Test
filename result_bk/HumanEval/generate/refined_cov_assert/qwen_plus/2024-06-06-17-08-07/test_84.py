from code_84 import solve

def test():
    assert solve(1000) == "1"
    assert solve(150) == "110"
    assert solve(147) == "1100"
    assert solve(2022) == "10110"
    assert solve(1024) == "1"
    assert solve(0) == "0"
    assert solve(1001) == "101"
    assert solve(9999) == "31"
    assert solve(500) == "1101"
    assert solve(4096) == "1"
