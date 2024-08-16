from code_81 import numerical_letter_grade
def test():   
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'C', 'C-', 'B', 'A-']
    assert numerical_letter_grade([1.0, 2.5, 3.7, 0.5, 2.0]) == ['D-', 'C+', 'A', 'E', 'C+']
    assert numerical_letter_grade([3.1, 2.8, 1.1, 2.4, 0.9]) == ['B', 'B-', 'E', 'C', 'D-']