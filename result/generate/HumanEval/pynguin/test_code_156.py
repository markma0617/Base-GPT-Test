# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_156 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = 'Z"1>'
    module_0.int_to_mini_roman(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    var_0 = module_0.int_to_mini_roman(none_type_0)
    assert var_0 == ""
    tuple_0 = ()
    var_1 = module_0.int_to_mini_roman(tuple_0)
    assert var_1 == ""
    var_2 = module_0.int_to_mini_roman(var_0)
    assert var_2 == ""
    str_0 = "/VWkzoZI$R"
    module_0.int_to_mini_roman(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 2174.595
    module_0.int_to_mini_roman(float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b""
    var_0 = module_0.int_to_mini_roman(bytes_0)
    assert var_0 == ""
    bool_0 = True
    none_type_0 = None
    var_1 = module_0.int_to_mini_roman(bool_0)
    assert var_1 == "i"
    var_2 = module_0.int_to_mini_roman(none_type_0)
    assert var_2 == ""
    module_0.int_to_mini_roman(var_1)
