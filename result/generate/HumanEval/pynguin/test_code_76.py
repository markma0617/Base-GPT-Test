# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_76 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    bool_1 = False
    var_0 = module_0.is_simple_power(bool_0, bool_1)
    int_0 = -2530
    var_1 = module_0.is_simple_power(int_0, bool_0)
    assert var_1 is False
    none_type_0 = None
    var_2 = module_0.is_simple_power(var_1, bool_1)
    assert var_2 is False
    var_3 = module_0.is_simple_power(var_1, none_type_0)
    assert var_3 is False


def test_case_1():
    int_0 = 4204
    var_0 = module_0.is_simple_power(int_0, int_0)
    assert var_0 is True


def test_case_2():
    bool_0 = False
    var_0 = module_0.is_simple_power(bool_0, bool_0)
    assert var_0 is False
    var_1 = module_0.is_simple_power(bool_0, var_0)
    none_type_0 = None
    var_2 = module_0.is_simple_power(var_1, none_type_0)
    assert var_2 is False


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1617
    int_1 = -1600
    var_0 = module_0.is_simple_power(int_0, int_1)
    var_1 = module_0.is_simple_power(int_0, int_0)
    assert var_1 is True
    var_2 = module_0.is_simple_power(int_0, var_1)
    assert var_2 is False
    var_3 = module_0.is_simple_power(var_2, int_0)
    assert var_3 is False
    none_type_0 = None
    var_4 = module_0.is_simple_power(none_type_0, var_1)
    assert var_4 is False
    var_5 = module_1.object()
    module_0.is_simple_power(int_0, none_type_0)
