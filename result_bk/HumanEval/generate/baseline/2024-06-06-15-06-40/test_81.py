from code_81 import numerical_letter_grade

import unittest

def numerical_letter_grade(grades):
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade


class TestNumericalLetterGrade(unittest.TestCase):

    def test_example(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'C', 'D', 'C', 'A-'])

    def test_all_grades(self):
        self.assertEqual(numerical_letter_grade([4.0, 3.8, 3.4, 3.1, 2.8, 2.4, 2.1, 1.8, 1.4, 1.1, 0.8, 0.5]), ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-'])

    def test_boundary_cases(self):
        self.assertEqual(numerical_letter_grade([4.0, 0.0]), ['A+', 'E'])


if __name__ == '__main__':
    unittest.main()
