from code_27 import flip_case

def test():
    assert flip_case("Hello") == "hELLO"
    assert flip_case("WORLD") == "wOrld"
    assert flip_case("Python") == "pYTHON"
    assert flip_case("Test") == "tEST"
    assert flip_case("aBcDeFg") == "AbCdEfG"
    assert flip_case("ZzZ") == "zzz"
    assert flip_case("12345!") == "12345!"
    assert flip_case("") == ""
    assert flip_case("   ") == "   "
    assert flip_case("AaBbCcDdEe") == "aAbBcCdDeE"
