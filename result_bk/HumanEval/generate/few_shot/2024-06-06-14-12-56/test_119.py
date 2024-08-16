from code_119 import check
from code_119 import match_parens

def test():
    assert match_parens(['()(', ')']) == 'Yes'
    assert match_parens([')', ')']) == 'No'
    assert match_parens(['(((', ')))']) == 'Yes'
    assert match_parens(['((((', ')))']) == 'No'
    assert match_parens(['()', ')']) == 'Yes'
