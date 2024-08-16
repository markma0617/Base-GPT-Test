from code_140 import fix_spaces

def test():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("Multiple  spaces  here") == "Multiple_-spaces-_here"
    assert fix_spaces("Consecutive__spaces") == "Consecutive___spaces"
    assert fix_spaces("End  space") == "End_-space"
    assert fix_spaces("Start space  ") == "_Start_space-"
    assert fix_spaces(" Middle spaces  ") == "_Middle_spaces-"
    assert fix_spaces("No_spaces_here") == "No_spaces_here"
    assert fix_spaces("Two__consecutive____spaces") == "Two__consecutive_-_spaces"
