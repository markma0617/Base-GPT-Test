# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import code_52 as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    list_0 = [object_0, object_0, object_0, object_0]
    bool_0 = True
    module_1.below_threshold(list_0, bool_0)


def test_case_1():
    list_0 = []
    var_0 = module_1.below_threshold(list_0, list_0)
    int_0 = -304
    var_1 = module_1.below_threshold(list_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -3660
    module_1.below_threshold(int_0, int_0)


def test_case_3():
    int_0 = -2973
    list_0 = [int_0]
    var_0 = module_1.below_threshold(list_0, int_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xf9\xfa\x19\x15\xccE\x8c\x85l\xc1\xc36\xf4c\x83\xfeE\xe5"
    int_0 = -1008
    list_0 = [bytes_0, bytes_0, int_0, int_0]
    int_1 = 967
    var_0 = module_1.below_threshold(bytes_0, int_1)
    assert var_0 is True
    int_2 = -175
    module_1.below_threshold(list_0, int_2)