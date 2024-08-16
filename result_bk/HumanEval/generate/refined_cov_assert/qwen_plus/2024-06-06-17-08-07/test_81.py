from code_81 import numerical_letter_grade

def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([4.0, 3.8, 2.3, 1.0, 3.7]) == ['A+', 'A', 'B-', 'D+', 'A']
    assert numerical_letter_grade([3.3, 3.0, 2.7, 2.3, 1.7]) == ['A-', 'B+', 'B', 'B-', 'C']
    assert numerical_letter_grade([2.0, 1.3, 1.0, 0.7, 0.0]) == ['C+', 'C-', 'D+', 'D', 'E']
    assert numerical_letter_grade([3.9, 3.6, 3.3, 3.0, 2.7]) == ['A+', 'A+', 'A-', 'B+', 'B']
    assert numerical_letter_grade([2.4, 2.8, 2.2, 2.6, 3.1]) == ['B-', 'B', 'B-', 'B+', 'A-']
    assert numerical_letter_grade([1.4, 1.8, 1.2, 1.6, 2.1]) == ['C-', 'C', 'C-', 'C+', 'C+']
    assert numerical_letter_grade([0.8, 1.2, 0.4, 0.6, 0.1]) == ['D', 'D+', 'E', 'D', 'E']
    assert numerical_letter_grade([4.0, 0.0, 3.7, 3.3, 3.0]) == ['A+', 'E', 'A', 'A-', 'B+']
    assert numerical_letter_grade([2.7, 2.3, 2.0, 1.7, 1.3]) == ['B', 'B-', 'C+', 'C', 'C-']
