# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_99 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "8"
    var_0 = module_0.closest_integer(str_0)
    assert var_0 == 8


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = 'n,L"\\#j%MsyZoE\\'
    module_0.closest_integer(str_0)


def test_case_2():
    str_0 = ".5"
    var_0 = module_0.closest_integer(str_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ".0"
    module_0.closest_integer(str_0)


def test_case_4():
    str_0 = "-.50"
    var_0 = module_0.closest_integer(str_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = ".500"
    var_0 = module_0.closest_integer(str_0)
    assert var_0 == 1
    object_0 = module_1.object()
    str_1 = "8"
    var_1 = module_0.closest_integer(str_1)
    assert var_1 == 8
    module_0.closest_integer(var_0)
