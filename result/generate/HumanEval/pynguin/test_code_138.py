# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_138 as module_0


def test_case_0():
    int_0 = -3448
    var_0 = module_0.is_equal_to_sum_even(int_0)
    assert var_0 is False
    var_1 = module_0.is_equal_to_sum_even(var_0)
    var_2 = module_0.is_equal_to_sum_even(int_0)
    assert var_2 is False
    var_3 = module_0.is_equal_to_sum_even(int_0)
    assert var_3 is False
    var_4 = module_0.is_equal_to_sum_even(var_3)


def test_case_1():
    float_0 = 1565.9
    float_1 = -3076.9
    var_0 = module_0.is_equal_to_sum_even(float_1)
    var_1 = module_0.is_equal_to_sum_even(float_0)
    assert var_1 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.is_equal_to_sum_even(none_type_0)
