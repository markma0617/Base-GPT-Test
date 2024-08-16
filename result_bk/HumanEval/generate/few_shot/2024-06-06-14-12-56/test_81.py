from code_81 import numerical_letter_grade

def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'C', 'C-', 'C', 'A-']
    assert numerical_letter_grade([3.9, 2.8, 2.1, 1.5, 0.7]) == ['A', 'B-', 'C+', 'D', 'D']
    assert numerical_letter_grade([3.3, 2.2, 1.0, 0.8, 0.0]) == ['A-', 'C+', 'D+', 'D', 'E']
    assert numerical_letter_grade([2.7, 1.8, 0.3, 2.5, 3.9]) == ['B', 'C', 'E', 'B-', 'A']
    assert numerical_letter_grade([2.0, 1.4, 3.7, 2.9, 0.9]) == ['C+', 'C-', 'A', 'B+', 'D']
