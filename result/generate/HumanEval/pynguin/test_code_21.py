# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_21 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "9aCQ]XBC8\rn Z}"
    module_0.rescale_to_unit(str_0)


def test_case_1():
    float_0 = 4558.0
    bool_0 = True
    set_0 = {float_0, bool_0, float_0}
    list_0 = module_0.rescale_to_unit(set_0)