# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import code_162 as module_0
'''
def test_case_0():
    str_0 = "\x0czw&%Vs{CH7#jWs"
    var_0 = module_0.string_to_md5(str_0)
    assert var_0 == "34d21c89a6602249ac73a17d76562c3c"
    bool_0 = True
    module_0.string_to_md5(bool_0)
'''

def test_case_1():
    tuple_0 = ()
    var_0 = module_0.string_to_md5(tuple_0)
    var_1 = module_0.string_to_md5(var_0)
    var_2 = module_0.string_to_md5(tuple_0)
    var_3 = module_0.string_to_md5(var_2)