from code_153 import Strongest_Extension

def test():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('class_1', ['extension1', 'EXTENSION2', 'ExteNsiOn3']) == 'class_1.EXTENSION2'
    assert Strongest_Extension('test', ['Test1', 'Test2', 'TeSt3']) == 'test.Test1'
