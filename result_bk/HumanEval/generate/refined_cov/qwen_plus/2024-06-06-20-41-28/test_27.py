from code_27 import flip_case

def test():
    assert flip_case("Hello") == "hELLO"
    assert flip_case("WORLD") == "wORLD"
    assert flip_case("FlipCase") == "fLIPcASE"
