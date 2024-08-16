from code_6 import parse_paren_group
from code_6 import parse_nested_parens

def test():   
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
