# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_43 as module_0


def test_case_0():
    str_0 = "5[E'BG2\""
    var_0 = module_0.pairs_sum_to_zero(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.pairs_sum_to_zero(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.pairs_sum_to_zero(list_0)
    assert var_0 is True
    module_0.pairs_sum_to_zero(var_0)