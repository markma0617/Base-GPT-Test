# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_47 as module_0


def test_case_0():
    tuple_0 = ()
    list_0 = [tuple_0]
    var_0 = module_0.median(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.median(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.median(none_type_0)