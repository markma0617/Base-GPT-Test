# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_83 as module_0


def test_case_0():
    bool_0 = True
    var_0 = module_0.starts_one_ends(bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "W$l?j\r"
    module_0.starts_one_ends(str_0)
