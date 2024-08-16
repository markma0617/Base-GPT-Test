from code_81 import numerical_letter_grade

def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([3.8, 2.7, 2.3, 1.0, 0.7]) == ['A-', 'B', 'B-', 'D+', 'D']
    assert numerical_letter_grade([4.0, 3.7, 3.3, 3.0, 2.7]) == ['A+', 'A', 'A-', 'B+', 'B']
