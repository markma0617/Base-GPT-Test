# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_96 as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.count_up_to(bool_0)
    bool_1 = False
    var_1 = module_0.count_up_to(bool_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ".Q$V'"
    module_0.count_up_to(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 19
    var_0 = module_0.count_up_to(int_0)
    var_1 = module_0.count_up_to(int_0)
    none_type_0 = None
    module_0.count_up_to(none_type_0)