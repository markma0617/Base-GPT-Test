# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_86 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "^#Fi&pG"
    var_0 = module_0.anti_shuffle(str_0)
    assert var_0 == "#&FG^ip"
    var_1 = module_0.anti_shuffle(var_0)
    assert var_1 == "#&FG^ip"
    str_1 = "|"
    var_2 = module_0.anti_shuffle(str_1)
    list_0 = [str_1]
    module_0.anti_shuffle(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    module_0.anti_shuffle(object_0)
