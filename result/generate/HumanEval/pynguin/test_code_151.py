# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_151 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    var_0 = module_0.double_the_difference(tuple_0)
    list_0 = [tuple_0]
    var_1 = module_0.double_the_difference(tuple_0)
    module_0.double_the_difference(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.double_the_difference(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xd1\x83"
    var_0 = module_0.double_the_difference(bytes_0)
    assert var_0 == 60842
    module_0.double_the_difference(var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.double_the_difference(dict_0)
    dict_1 = {}
    bytes_0 = b"\x18\\\x9fx"
    tuple_0 = (dict_1, bytes_0)
    module_0.double_the_difference(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"Z/\xe8\x16\xdd\x96\xab\xb3\xe1&\x83\xda\xbd\xd3\xf26"
    var_0 = module_0.double_the_difference(bytes_0)
    assert var_0 == 260360
    str_0 = "G\n="
    module_0.double_the_difference(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 329.0
    bool_0 = True
    tuple_0 = (float_0, bool_0, bool_0)
    var_0 = module_0.double_the_difference(tuple_0)
    assert var_0 == 2
    int_0 = 669
    module_0.double_the_difference(int_0)
