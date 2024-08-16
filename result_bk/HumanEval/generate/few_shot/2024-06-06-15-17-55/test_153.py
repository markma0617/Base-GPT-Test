from code_153 import Strongest_Extension

def test():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('Test', ['test', 'TesT', 'TEST']) == 'Test.TesT'
    assert Strongest_Extension('Example', ['exAmple', 'EXAMPL', 'exAmPLE']) == 'Example.exAmple'
    assert Strongest_Extension('Extension', ['exT', 'eXT', 'XT']) == 'Extension.eXT'
