# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_51 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"c\xfeb\x1eX\xc0\xe90\xc0\xc5#s\xcbG\xfd\x93o"
    module_0.remove_vowels(bytes_0)


def test_case_1():
    str_0 = "m`jXk,H))vYXh\r*/<b"
    set_0 = {str_0, str_0}
    var_0 = module_0.remove_vowels(set_0)
    assert var_0 == "m`jXk,H))vYXh\r*/<b"


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -3414
    module_0.remove_vowels(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "2ek"
    var_0 = module_0.remove_vowels(str_0)
    assert var_0 == "2k"
    var_1 = module_0.remove_vowels(str_0)
    assert var_1 == "2k"
    object_0 = module_1.object()
    module_0.remove_vowels(object_0)