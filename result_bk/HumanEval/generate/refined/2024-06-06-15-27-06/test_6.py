from code_6 import parse_nested_parens
def test():
    assert parse_nested_parens('()') == [1]
    assert parse_nested_parens('()()') == [1, 1]
    assert parse_nested_parens('(())(())()') == [2, 2, 1]