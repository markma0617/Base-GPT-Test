# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_112 as module_0


def test_case_0():
    str_0 = "v:*R^z1G"
    var_0 = module_0.reverse_delete(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.reverse_delete(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Q%+`V{XyiST(j"
    str_1 = ':xd<OVaj*Ap\x0b@;@"ORS'
    var_0 = module_0.reverse_delete(str_0, str_1)
    module_0.reverse_delete(var_0, str_1)
