# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_59 as module_0


def test_case_0():
    int_0 = 128
    var_0 = module_0.largest_prime_factor(int_0)
    assert var_0 == 2


def test_case_1():
    bool_0 = True
    var_0 = module_0.largest_prime_factor(bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x01\x87\xbc\xd9\x84\x94\xee\xac\xc2?2"
    module_0.largest_prime_factor(bytes_0)


def test_case_3():
    int_0 = 118
    var_0 = module_0.largest_prime_factor(int_0)
    assert var_0 == 59
