# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_82 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    var_0 = module_0.prime_length(list_0)
    assert var_0 is False
    none_type_0 = None
    module_0.prime_length(none_type_0)


def test_case_1():
    set_0 = set()
    tuple_0 = (set_0,)
    var_0 = module_0.prime_length(tuple_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.prime_length(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "%i1^</KK&Vb.\tXF"
    var_0 = module_0.prime_length(str_0)
    assert var_0 is False
    var_1 = module_0.prime_length(str_0)
    assert var_1 is False
    var_2 = module_0.prime_length(str_0)
    assert var_2 is False
    int_0 = 394
    module_0.prime_length(int_0)


def test_case_4():
    bytes_0 = b"j5\xdc@\x90\xc8\x94r\x16\xf3@\x1e\xda'\x1f"
    int_0 = 2214
    set_0 = {int_0, bytes_0, int_0, int_0}
    var_0 = module_0.prime_length(set_0)
    assert var_0 is True
