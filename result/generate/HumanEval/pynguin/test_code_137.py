# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_137 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "TY\na(+BN(MA~~ZTyMl/\x0c"
    module_0.compare_one(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    module_0.compare_one(tuple_0, tuple_0)


def test_case_2():
    bool_0 = False
    var_0 = module_0.compare_one(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -192.73
    var_0 = module_0.compare_one(float_0, float_0)
    var_1 = module_0.compare_one(float_0, float_0)
    float_1 = -2781.5
    var_2 = module_0.compare_one(float_0, float_1)
    assert var_2 == pytest.approx(-192.73, abs=0.01, rel=0.01)
    module_0.compare_one(var_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -2781.5
    var_0 = module_0.compare_one(float_0, float_0)
    var_1 = module_0.compare_one(float_0, float_0)
    float_1 = -272.6599
    var_2 = module_0.compare_one(float_0, float_1)
    assert var_2 == pytest.approx(-272.6599, abs=0.01, rel=0.01)
    module_0.compare_one(var_1, var_1)