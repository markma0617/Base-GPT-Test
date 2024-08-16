from code_153 import Strongest_Extension

def test():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('A', ['B', 'C', 'D']) == 'A.B'
    assert Strongest_Extension('X', ['xYz', 'abc', 'DEF']) == 'X.DEF'
    assert Strongest_Extension('Test', ['ABcDeF', 'GhIjKl', 'MnOpQ']) == 'Test.ABcDeF'
    assert Strongest_Extension('One', ['ONE', 'two', 'Three']) == 'One.ONE'
    assert Strongest_Extension('First', ['second', 'THird', 'FOURTH']) == 'First.FOURTH'
    assert Strongest_Extension('Class', ['class', 'CLaSS', 'clASs']) == 'Class.CLaSS'
    assert Strongest_Extension('Name', ['NAME', 'name', 'NaMe']) == 'Name.NAME'
    assert Strongest_Extension('Alpha', ['beta', 'GAMMA', 'delta']) == 'Alpha.GAMMA'
