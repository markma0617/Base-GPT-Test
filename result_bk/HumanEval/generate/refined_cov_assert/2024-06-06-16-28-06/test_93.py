from code_93 import encode
def test():
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert encode('HELLO') == 'HJLLO'
    assert encode('python') == 'pJthpn'
    assert encode('AEIOU') == 'CJMQW'
    assert encode('abcdefghijklmnopqrstuvwxyz') == 'bcdEfghIjklmnOpqrstUvwxyz'
    assert encode('AbCdEfGhIjKlMnOpQrStUvWxYz') == 'bdCdGfHjLmNpQrStVxYz'
    assert encode('ThIs Is A TeSt') == 'tJKs Ks C TgSt'
    assert encode('hello world') == 'hJllo wrld'
    assert encode('I Love Python') == 'k Lqxg Rjvkpq'
