# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_13 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb2K\xf0\x1ab8\x93"
    module_0.greatest_common_divisor(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    int_0 = module_0.greatest_common_divisor(bool_0, bool_0)
    assert int_0 is False
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    none_type_0 = None
    module_0.greatest_common_divisor(none_type_0, tuple_0)


def test_case_2():
    bool_0 = True
    int_0 = module_0.greatest_common_divisor(bool_0, bool_0)
    bool_1 = True
    int_1 = -3474
    int_2 = module_0.greatest_common_divisor(bool_1, int_1)
    assert int_2 == -1
    int_3 = module_0.greatest_common_divisor(bool_1, bool_1)