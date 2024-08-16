from code_81 import numerical_letter_grade

def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'C', 'C-', 'C+', 'A-']
    assert numerical_letter_grade([3.9, 2.8, 1.5, 4.0]) == ['A', 'B', 'D+', 'A+']
    assert numerical_letter_grade([2.6, 3.2, 1.1, 0.5]) == ['C', 'B-', 'D-', 'E']
    assert numerical_letter_grade([]) == []
