from code_77 import iscube

def test():
    assert iscube(1) == True
    assert iscube(2) == False
    assert iscube(-1) == True
