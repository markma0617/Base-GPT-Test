# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_110 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xfa[\xe9H/\x1e\xd9\xb1\xcdN\x85\xe1\x00\xf9"
    var_0 = module_0.exchange(bytes_0, bytes_0)
    assert var_0 == "NO"
    module_0.exchange(bytes_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    var_0 = module_0.exchange(list_0, list_0)
    assert var_0 == "YES"
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    var_0 = module_0.exchange(list_0, list_0)
    assert var_0 == "YES"
    var_1 = module_0.exchange(list_0, list_0)
    assert var_1 == "YES"
    var_2 = module_0.exchange(list_0, list_0)
    assert var_2 == "YES"
    module_0.exchange(var_2, var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -42
    module_0.exchange(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 944
    tuple_0 = (int_0,)
    module_0.exchange(tuple_0, int_0)
