from code_153 import Strongest_Extension

def test():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('class_name', ['MyExtension', 'NotStrong', 'STRongEST']) == 'class_name.STRongEST'
    assert Strongest_Extension('test', ['a', 'b', 'c']) == 'test.a'
