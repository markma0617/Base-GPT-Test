# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_136 as module_0


def test_case_0():
    bytes_0 = b"\x9d\x9e}\x03Lc\xe5S\xbc[\x8a5\x8a\x00\xce\xf0\xe1{OF"
    var_0 = module_0.largest_smallest_integers(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    var_0 = module_0.largest_smallest_integers(str_0)
    module_0.largest_smallest_integers(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.largest_smallest_integers(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1966
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.largest_smallest_integers(dict_0)
    bool_0 = True
    dict_1 = {bool_0: bool_0}
    var_1 = module_0.largest_smallest_integers(dict_1)
    module_0.largest_smallest_integers(var_1)