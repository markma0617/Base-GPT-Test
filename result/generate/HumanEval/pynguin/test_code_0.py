# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_0 as module_0
import builtins as module_1


def test_case_0():
    int_0 = -990
    list_0 = [int_0]
    bool_0 = module_0.has_close_elements(list_0, list_0)
    assert bool_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -2155.274
    list_0 = [float_0, float_0, float_0, float_0]
    bool_0 = True
    bool_1 = module_0.has_close_elements(list_0, bool_0)
    assert bool_1 is True
    object_0 = module_1.object()
    set_0 = {object_0}
    tuple_0 = (object_0, set_0)
    module_0.has_close_elements(tuple_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -479.081095
    float_1 = 2006.4
    list_0 = [float_0, float_0, float_0, float_1]
    bool_0 = module_0.has_close_elements(list_0, float_0)
    assert bool_0 is False
    none_type_0 = None
    module_0.has_close_elements(none_type_0, float_0)