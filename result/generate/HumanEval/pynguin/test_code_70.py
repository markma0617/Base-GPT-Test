# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_70 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x93\xcb\xad\xbd\xbd@Hr\x08v\xc8\x97\xcd\xd2\xd1\x8ez\xbb\r\xb3"
    module_0.strange_sort_list(bytes_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.strange_sort_list(none_type_0)
    var_1 = module_0.strange_sort_list(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -371
    tuple_0 = (int_0,)
    set_0 = {tuple_0}
    var_0 = module_0.strange_sort_list(set_0)
    bytes_0 = b"e\x10X4=_\xf1"
    module_0.strange_sort_list(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    var_0 = module_0.strange_sort_list(tuple_0)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    var_1 = module_0.strange_sort_list(list_0)
    int_0 = -371
    module_0.strange_sort_list(int_0)