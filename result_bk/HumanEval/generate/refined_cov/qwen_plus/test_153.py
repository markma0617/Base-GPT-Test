from code_153 import Strongest_Extension

def test():
    assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension("Sample", ['BaNaNa', 'apple', 'cherry']) == 'Sample.BaNaNa'
    assert Strongest_Extension("Case", ['CAPital', 'lowerCASE', 'Mixed']) == 'Case.CAPital'
    assert Strongest_Extension("Test", ['EQUAL', 'equal', 'EQUAL']) == 'Test.EQUAL'
    assert Strongest_Extension("NoCase", ['allLOW', 'UPPER', 'MiXed']) == 'NoCase.UPPER'
