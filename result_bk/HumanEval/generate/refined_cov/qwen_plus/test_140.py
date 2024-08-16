from code_140 import fix_spaces

def test():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("Many   spaces  here") == "Many-spaces-here"
    assert fix_spaces("No_space_here") == "No_space_here"
    assert fix_spaces("Consecutive___spaces") == "Consecutive_spaces"
