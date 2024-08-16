from code_93 import encode
def test():   
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert encode('HELLO') == 'JGNNQ'
    assert encode('encode me') == 'GNGDGA OG'
    assert encode('aeiou') == 'CGKQM'