# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_140 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "Au$ MR<S~`2;R)|o_o=\n"
    var_0 = module_0.fix_spaces(str_0)
    assert var_0 == "Au$_MR<S~`2;R)|o_o=\n"


def test_case_1():
    list_0 = []
    var_0 = module_0.fix_spaces(list_0)
    assert var_0 == ""
    var_1 = module_0.fix_spaces(var_0)
    assert var_1 == ""
    var_2 = module_0.fix_spaces(list_0)
    assert var_2 == ""
    str_0 = "m8'tG1Z|..9$6ZlBhX5"
    var_3 = module_0.fix_spaces(str_0)
    assert var_3 == "m8'tG1Z|..9$6ZlBhX5"
    var_4 = module_0.fix_spaces(var_2)
    assert var_4 == ""
    var_5 = module_0.fix_spaces(var_3)
    assert var_5 == "m8'tG1Z|..9$6ZlBhX5"
    var_6 = module_0.fix_spaces(var_1)
    assert var_6 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.fix_spaces(bool_0)


def test_case_3():
    str_0 = "G\x0c "
    object_0 = module_0.fix_spaces(str_0)
    assert object_0 == "G\x0c_"


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "  "
    var_0 = module_0.fix_spaces(str_0)
    assert var_0 == "_"
    var_1 = module_0.fix_spaces(str_0)
    assert var_1 == "_"
    list_0 = [var_1, str_0, str_0]
    var_2 = module_0.fix_spaces(list_0)
    assert var_2 == "_    "
    str_1 = "R"
    var_3 = module_0.fix_spaces(str_1)
    assert var_3 == "R"
    var_4 = module_0.fix_spaces(var_2)
    assert var_4 == "_-"
    var_5 = module_0.fix_spaces(list_0)
    assert var_5 == "_    "
    module_1.object(*str_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "  "
    var_0 = module_0.fix_spaces(str_0)
    assert var_0 == "_"
    var_1 = module_0.fix_spaces(str_0)
    assert var_1 == "_"
    list_0 = [var_1, str_0, str_0, var_0]
    var_2 = module_0.fix_spaces(list_0)
    assert var_2 == "_    _"
    str_1 = "R"
    var_3 = module_0.fix_spaces(str_1)
    assert var_3 == "R"
    var_4 = module_0.fix_spaces(var_2)
    assert var_4 == "_-_"
    var_5 = module_0.fix_spaces(list_0)
    assert var_5 == "_    _"
    module_1.object(*str_1)
