# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_134 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = '"\\'
    var_0 = module_0.check_if_last_char_is_a_letter(str_0)
    assert var_0 is False
    none_type_0 = None
    module_0.check_if_last_char_is_a_letter(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.check_if_last_char_is_a_letter(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "U"
    var_0 = module_0.check_if_last_char_is_a_letter(str_0)
    assert var_0 is True
    var_1 = module_1.object()
    object_0 = module_1.object()
    module_0.check_if_last_char_is_a_letter(object_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "*"
    var_0 = module_0.check_if_last_char_is_a_letter(str_0)
    assert var_0 is False
    object_0 = module_1.object()
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "{"
    var_0 = module_0.check_if_last_char_is_a_letter(str_0)
    assert var_0 is False
    module_0.check_if_last_char_is_a_letter(var_0)