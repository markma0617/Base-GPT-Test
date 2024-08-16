from code_81 import numerical_letter_grade

def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'C', 'C-', 'C', 'A-']
    assert numerical_letter_grade([3.0, 2.7, 1.5, 0.7, 3.8]) == ['B+', 'B', 'D+', 'D', 'A']
    assert numerical_letter_grade([2.0, 2.3, 0.0, 1.1, 0.5]) == ['C+', 'B-', 'E', 'D', 'E']
