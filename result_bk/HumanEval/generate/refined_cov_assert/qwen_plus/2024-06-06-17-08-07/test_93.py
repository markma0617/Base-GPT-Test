from code_93 import encode

def test():
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert encode('Python is fun') == 'PythN nS fMM'
    assert encode('Encode this') == 'EnCD TGX'
    assert encode('Hello world') == 'HLLW RLD'
    assert encode('A quick brown dog') == 'C qUIK BrWN DG'
    assert encode('Python3 is awesome') == 'PythN3 nS AwSM'
    assert encode('vowels are replaced') == 'vGwls rE PCd'
    assert encode('AEIOUaeiou') == 'CGHKcghk'
    assert encode('Xyz') == 'XyZ'
