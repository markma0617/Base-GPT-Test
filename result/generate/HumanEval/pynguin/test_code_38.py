# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_38 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    module_0.decode_cyclic(dict_0)


def test_case_1():
    str_0 = 'L}H9?]D-!(Y"+4`\t5\x0b/9'
    var_0 = module_0.encode_cyclic(str_0)
    assert var_0 == '}HL?]9-!DY"(4`+5\x0b\t/9'
    str_1 = "Thro9"
    var_1 = module_0.encode_cyclic(str_1)
    assert var_1 == "hrTo9"
