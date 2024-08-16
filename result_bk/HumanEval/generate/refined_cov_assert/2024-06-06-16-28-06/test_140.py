from code_140 import fix_spaces

def test():   
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces(" 4 5 6") == "_4-5_6"
    assert fix_spaces("   7  8  9") == "-7-8-9"
    assert fix_spaces("") == ""
    assert fix_spaces("A B  C   D    E") == "A_B-C-_D-_E"
    assert fix_spaces(" A  B  C  D  E ") == "_A-_B-_C-_D-_E_"
    assert fix_spaces("   One Two Three  ") == "-One_Two_Three-"
