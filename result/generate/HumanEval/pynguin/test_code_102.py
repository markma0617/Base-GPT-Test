# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import code_102 as module_0


def test_case_0():
    float_0 = -25.41
    var_0 = module_0.choose_num(float_0, float_0)
    assert var_0 == -1
    var_1 = module_0.choose_num(float_0, float_0)
    assert var_1 == -1
    var_2 = module_0.choose_num(var_1, float_0)
    assert var_2 == -1
    var_3 = module_0.choose_num(var_2, float_0)
    assert var_3 == -1


def test_case_1():
    bool_0 = False
    var_0 = module_0.choose_num(bool_0, bool_0)
    assert var_0 is False


def test_case_2():
    float_0 = -2635.0717
    var_0 = module_0.choose_num(float_0, float_0)
    assert var_0 == -1


def test_case_3():
    float_0 = 637.4
    var_0 = module_0.choose_num(float_0, float_0)
    assert var_0 == -1
    var_1 = module_0.choose_num(float_0, var_0)
    assert var_1 == -1
    bool_0 = True
    var_2 = module_0.choose_num(bool_0, bool_0)
    assert var_2 == -1
    var_3 = module_0.choose_num(bool_0, bool_0)
    assert var_3 == -1
    int_0 = -1991
    var_4 = module_0.choose_num(var_2, bool_0)
    assert var_4 == 0
    var_5 = module_0.choose_num(int_0, var_3)
    assert var_5 == -2
    bool_1 = False
    var_6 = module_0.choose_num(bool_1, bool_1)
    assert var_6 is False
