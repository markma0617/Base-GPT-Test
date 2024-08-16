from code_153 import Strongest_Extension

def test():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('test_class', ['Lowercase', 'UPPERCASE', 'MixedCase']) == 'test_class.UPPERCASE'
