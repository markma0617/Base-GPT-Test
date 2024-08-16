from code_27 import flip_case
def test():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('HeLLo') == 'hEllO'
    assert flip_case('hElLo') == 'HeLlO'