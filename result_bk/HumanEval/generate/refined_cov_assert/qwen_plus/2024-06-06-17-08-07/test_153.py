from code_153 import Strongest_Extension

def test():
    assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension("Sample", ['BaNaNa', 'MaNgo', 'apple']) == 'Sample.BaNaNa'
    assert Strongest_Extension("ClassName", ['EXTENSION1', 'extension2', 'EXTENSION3']) == 'ClassName.EXTENSION1'
    assert Strongest_Extension("Test", ['AbcD', 'eFGh', 'ijKL']) == 'Test.eFGh'
    assert Strongest_Extension("Case", ['AllCAPS', 'allLower', 'MixedCase']) == 'Case.MixedCase'
    assert Strongest_Extension("NoCaseDiff", ['abc123', 'ABC123', 'abcABC']) == 'NoCaseDiff.abc123'
    assert Strongest_Extension("EqualStrength", ['xyZ', 'YZX', 'zXY']) == 'EqualStrength.xyZ'
    assert Strongest_Extension("Class", ['Same', 'SAME', 'same']) == 'Class.Same'
    assert Strongest_Extension("Longest", ['AAAbb', 'ccDD', 'eeFFgg']) == 'Longest.AAAbb'
    assert Strongest_Extension("Empty", []) == 'Empty.Empty'
