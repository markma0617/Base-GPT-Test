from code_81 import numerical_letter_grade

def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'C', 'C-', 'B', 'A-']
    assert numerical_letter_grade([3.0, 2.0, 1.7, 0.3, 4.0]) == ['B+', 'C+', 'C', 'E', 'A+']
    assert numerical_letter_grade([2.0, 2.7, 1.3, 0.7, 3.7]) == ['C+', 'B', 'C-', 'D', 'A']
