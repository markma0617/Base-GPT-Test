from code_1 import separate_paren_groups
def test():   
    assert separate_paren_groups("( )") == ['()']
    assert separate_paren_groups("(( ))") == ['(())']
    assert separate_paren_groups("(( )( ))") == ['(()())']
    assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
    assert separate_paren_groups("( ) (( )( )) (( ))") == ['()', '(()())', '(())']
    assert separate_paren_groups("( ( ) ( )( )) (( ))") == ['( () () )', '(()())', '(())']
    assert separate_paren_groups("( ) ( ) ( )") == ['()', '()', '()']
    assert separate_paren_groups("( ) (( )( )) ( )") == ['()', '( () () )', '()']
    assert separate_paren_groups("( ) (( )( )) (( )( ))") == ['()', '( () () )', '(()())']
    assert separate_paren_groups("( ( ) ( )( )) (( )( ))") == ['( () () )', '( () () )', '(()())']