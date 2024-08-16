from code_81 import numerical_letter_grade
def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'C', 'C-', 'B', 'A-']
    assert numerical_letter_grade([3.0, 2.5, 1.0, 4.0, 2.7]) == ['B+', 'B-', 'D-', 'A+', 'B']
    assert numerical_letter_grade([2.3, 1.7, 3.9, 2.0]) == ['B-', 'C', 'A', 'C+']  