# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_95 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "2@'#Oc@"
    dict_0 = {str_0: str_0}
    var_0 = module_0.check_dict_case(dict_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.check_dict_case(bool_0)


def test_case_2():
    str_0 = "2@'#c@"
    dict_0 = {str_0: str_0}
    var_0 = module_0.check_dict_case(dict_0)
    assert var_0 is True
    dict_1 = {var_0: dict_0}
    var_1 = module_0.check_dict_case(dict_1)
    assert var_1 is False


def test_case_3():
    dict_0 = {}
    var_0 = module_0.check_dict_case(dict_0)
    var_1 = module_1.object()


def test_case_4():
    str_0 = "2@p'#c@"
    dict_0 = {str_0: str_0}
    var_0 = module_0.check_dict_case(dict_0)
    assert var_0 is True


def test_case_5():
    str_0 = ">~}S~PS("
    dict_0 = {str_0: str_0}
    var_0 = module_0.check_dict_case(dict_0)
    assert var_0 is True


def test_case_6():
    str_0 = "midi"
    str_1 = 'u^"'
    dict_0 = {str_0: str_1, str_1: str_1}
    var_0 = module_0.check_dict_case(dict_0)
    assert var_0 is True


def test_case_7():
    str_0 = "mixdi"
    str_1 = "u@peD"
    dict_0 = {str_0: str_1, str_1: str_1}
    var_0 = module_0.check_dict_case(dict_0)
    assert var_0 is False


def test_case_8():
    str_0 = "#A(C"
    str_1 = "upper"
    dict_0 = {str_0: str_1, str_1: str_1}
    var_0 = module_0.check_dict_case(dict_0)
    assert var_0 is False


def test_case_9():
    str_0 = ":I\r6"
    str_1 = 'N^";'
    dict_0 = {str_1: str_1, str_0: str_0, str_1: str_1}
    var_0 = module_0.check_dict_case(dict_0)
    assert var_0 is True