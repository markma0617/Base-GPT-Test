from code_19 import sort_numbers

def test():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('nine eight seven') == 'seven eight nine'
    assert sort_numbers('two four six') == 'two four six'
    assert sort_numbers('zero one nine eight') == '零 one eight nine'
    assert sort_numbers('five four three two one') == 'one two three four five'
    assert sort_numbers('nine nine nine nine') == 'nine nine nine nine'
    assert sort_numbers('eight six eight six') == 'six eight eight six'
    assert sort_numbers('three seven five nine one') == 'one three five seven nine'
    assert sort_numbers('zero zero zero') == 'zero zero zero'
    assert sort_numbers('random nonnumeric string') == 'random nonnumeric string'
