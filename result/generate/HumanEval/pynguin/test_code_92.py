# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import code_92 as module_0


def test_case_0():
    bool_0 = True
    var_0 = module_0.any_int(bool_0, bool_0, bool_0)
    assert var_0 is False


def test_case_1():
    float_0 = 69.96289
    bool_0 = True
    var_0 = module_0.any_int(float_0, float_0, bool_0)


def test_case_2():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.any_int(bool_0, none_type_0, none_type_0)
    assert var_0 is False
    var_1 = module_0.any_int(bool_0, bool_0, bool_0)
    assert var_1 is False


def test_case_3():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.any_int(bool_0, none_type_0, none_type_0)
    assert var_0 is False
    var_1 = module_0.any_int(bool_0, bool_0, none_type_0)
    var_2 = module_0.any_int(bool_0, bool_0, bool_0)
    assert var_2 is False


def test_case_4():
    dict_0 = {}
    list_0 = [dict_0]
    var_0 = module_0.any_int(list_0, dict_0, list_0)
    assert var_0 is False
    var_1 = module_0.any_int(var_0, var_0, var_0)
    assert var_1 is True
    var_2 = module_0.any_int(list_0, dict_0, dict_0)
    none_type_0 = None
    var_3 = module_0.any_int(none_type_0, none_type_0, none_type_0)


def test_case_5():
    bool_0 = True
    var_0 = module_0.any_int(bool_0, bool_0, bool_0)
    assert var_0 is False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    none_type_0 = None
    var_1 = module_0.any_int(dict_0, none_type_0, dict_0)
    assert var_1 is False
    var_2 = module_0.any_int(var_1, none_type_0, none_type_0)
    assert var_2 is False
    bool_1 = False
    none_type_1 = None
    str_0 = "s]rl%w6,h!"
    var_3 = module_0.any_int(str_0, var_1, dict_0)
    var_4 = module_0.any_int(bool_1, bool_1, none_type_1)
    bool_2 = True
    bool_3 = False
    none_type_2 = None
    var_5 = module_0.any_int(none_type_2, none_type_2, none_type_2)
    var_6 = module_0.any_int(bool_3, bool_1, none_type_2)
    var_7 = module_0.any_int(bool_2, var_6, none_type_2)
    var_8 = module_0.any_int(bool_2, bool_2, bool_3)
    assert var_8 is True
    var_9 = module_0.any_int(bool_1, bool_1, bool_2)
    assert var_9 is False
    none_type_3 = None
    bool_4 = True
    var_10 = module_0.any_int(bool_2, bool_1, bool_4)
    assert var_10 is True
    var_11 = module_0.any_int(bool_1, none_type_3, bool_4)
    var_12 = module_0.any_int(none_type_1, bool_3, dict_0)
