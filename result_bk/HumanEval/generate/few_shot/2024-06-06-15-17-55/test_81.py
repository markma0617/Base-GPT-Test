from code_81 import numerical_letter_grade

def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'C', 'C-', 'B', 'A-']
    assert numerical_letter_grade([3.9, 2, 1.4, 2.5, 3.1]) == ['A', 'C', 'D+', 'C', 'B-']
    assert numerical_letter_grade([2.5, 0.9, 3.6, 1.8, 2.1]) == ['B-', 'D-', 'A-', 'C', 'C+']
    assert numerical_letter_grade([0.3, 1.2, 2.9, 3.2, 4.0]) == ['E', 'D+', 'B', 'B', 'A+']
    assert numerical_letter_grade([1.7, 3.4, 2.8, 1.1, 0.0]) == ['C', 'A-', 'B-', 'D+', 'E']
