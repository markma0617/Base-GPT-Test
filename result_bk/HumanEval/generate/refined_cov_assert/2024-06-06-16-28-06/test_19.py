from code_19 import sort_numbers
def test():
    assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('five two four eight one six three nine seven zero') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('one three five nine two four six eight zero seven') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('three five two one nine seven six four zero eight') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('seven two nine four eight three six five one zero') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('two eight one five six zero four nine seven three') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('four six seven zero nine two five eight three one') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('eight zero six two five seven one three four nine') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('six nine zero five three four one eight seven two') == 'zero one two three four five six seven eight nine'