# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_9 as module_0


def test_case_0():
    int_0 = -272
    list_0 = [int_0]
    list_1 = module_0.rolling_max(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    list_1 = module_0.rolling_max(list_0)
    module_0.rolling_max(bool_0)
