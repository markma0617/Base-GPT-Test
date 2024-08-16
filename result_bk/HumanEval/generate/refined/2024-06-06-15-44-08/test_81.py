from code_81 import numerical_letter_grade
def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'C', 'C-', 'C', 'A-']
    assert numerical_letter_grade([3.0, 2.5, 0.7, 1.3, 2.7]) == ['B+', 'C+', 'D', 'C-', 'B']
    assert numerical_letter_grade([4.0, 0.5, 1.8, 3.3, 2.2]) == ['A+', 'E', 'D', 'A-', 'C']