# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_114 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ":,6F"
    bool_0 = True
    set_0 = {str_0, bool_0}
    module_0.minSubArraySum(set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.minSubArraySum(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -101.08
    list_0 = [float_0, float_0]
    var_0 = module_0.minSubArraySum(list_0)
    assert var_0 == pytest.approx(-202.16, abs=0.01, rel=0.01)
    dict_0 = {}
    module_0.minSubArraySum(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xe1\x03.1\x93\x98\x9aX\xd9\xcel^"
    var_0 = module_0.minSubArraySum(bytes_0)
    assert var_0 == 3
    bool_0 = False
    module_0.minSubArraySum(bool_0)
