# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_108 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -1.70393
    int_0 = 587
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, int_0: float_0}
    module_0.count_nums(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xec"
    var_0 = module_0.count_nums(bytes_0)
    assert var_0 == 1
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_1.object(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 2304
    set_0 = {int_0}
    list_0 = [set_0, set_0]
    module_0.count_nums(list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    set_0 = set()
    int_0 = -2074
    list_0 = [int_0]
    var_0 = module_0.count_nums(set_0)
    tuple_0 = (set_0, int_0, list_0, int_0)
    module_0.count_nums(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    object_0 = module_1.object()
    module_0.count_nums(object_0)
