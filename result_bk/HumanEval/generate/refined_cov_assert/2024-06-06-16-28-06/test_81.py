from code_81 import numerical_letter_grade

def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'C', 'C-', 'B', 'A-']
    assert numerical_letter_grade([3.8, 2.1, 1.0, 3.9, 3.3]) == ['A', 'C+', 'D-', 'A+', 'A-']
    assert numerical_letter_grade([2.9, 1.2, 0.5, 2.7]) == ['B', 'D', 'E', 'C']
    assert numerical_letter_grade([0.9, 3.7, 2.2, 2.4, 1.5]) == ['D', 'A', 'C+', 'B-', 'D+']
    assert numerical_letter_grade([]) == []
    assert numerical_letter_grade([4.0]) == ['A+']
    assert numerical_letter_grade([0.0]) == ['E']
    assert numerical_letter_grade([1.5, 3.2, 2.8]) == ['D', 'B', 'C']
    assert numerical_letter_grade([2.0, 2.1, 2.2, 2.3, 2.4]) == ['C+', 'C+', 'C+', 'C+', 'C+']
    assert numerical_letter_grade([3.5, 3.6, 3.4]) == ['A-', 'A-', 'A-']
