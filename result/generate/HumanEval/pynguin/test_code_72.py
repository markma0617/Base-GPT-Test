# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_72 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.will_it_fly(bool_0, bool_0)


def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.will_it_fly(dict_0, bool_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.will_it_fly(dict_0, bool_0)
    assert var_0 is True
    object_0 = module_1.object()
    float_0 = -4044.509
    var_1 = module_0.will_it_fly(dict_0, float_0)
    assert var_1 is False
    module_0.will_it_fly(bool_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    float_0 = 2894.6268
    var_0 = module_0.will_it_fly(list_0, float_0)
    assert var_0 is True
    module_0.will_it_fly(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 2006.32755
    int_0 = -2447
    tuple_0 = (float_0, int_0)
    var_0 = module_0.will_it_fly(tuple_0, float_0)
    assert var_0 is False
    none_type_0 = None
    module_0.will_it_fly(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0]
    float_0 = 2894.6268
    var_0 = module_0.will_it_fly(list_0, float_0)
    assert var_0 is True
    module_0.will_it_fly(var_0, var_0)