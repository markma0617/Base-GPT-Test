from code_1 import separate_paren_groups

def test():
    assert separate_paren_groups("( )") == ['()']
    assert separate_paren_groups("(( ))") == ['(())']
    assert separate_paren_groups("(( )( ))") == ['(()())']
    assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
    assert separate_paren_groups("(a)(b)(c)") == ['(a)', '(b)', '(c)']
    assert separate_paren_groups(" ((a)) ((b)(c)) ((d) )") == [' (a) ', ' (b)(c) ', ' (d) ']
    assert separate_paren_groups("((a)(b))((c)(d)(e))") == ['((a)(b))', '((c)(d)(e))']
    assert separate_paren_groups("(a)( (b) (c) )") == ['(a)', '( (b) (c) )']
    assert separate_paren_groups("(a)(b)(c(d)e(f))") == ['(a)', '(b)', '(c(d)e(f))']
    assert separate_paren_groups("(a)(b)(c(d)(e))") == ['(a)', '(b)', '(c(d)(e))']
