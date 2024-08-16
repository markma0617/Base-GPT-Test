from code_27 import flip_case
def test():   
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('heLLo') == 'HEllO'
    assert flip_case('hElLo') == 'HeLlO'