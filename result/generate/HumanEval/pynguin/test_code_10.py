# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import code_10 as module_0


def test_case_0():
    str_0 = "Hf3n"
    str_1 = module_0.make_palindrome(str_0)
    assert str_1 == "Hf3n3fH"


def test_case_1():
    none_type_0 = None
    str_0 = module_0.make_palindrome(none_type_0)
    assert str_0 == ""


def test_case_2():
    str_0 = "K%:\x0b~>\x0bxz"
    str_1 = module_0.make_palindrome(str_0)
    assert str_1 == "K%:\x0b~>\x0bxzx\x0b>~\x0b:%K"
    str_2 = "L"
    bool_0 = module_0.is_palindrome(str_2)
    str_3 = module_0.make_palindrome(str_2)
    assert str_3 == "L"
    str_4 = "#'m`EvhH\n "
    str_5 = module_0.make_palindrome(str_2)
    assert str_5 == "L"
    str_6 = "0<>G!2\t-Z7\tQT&~bj"
    str_7 = module_0.make_palindrome(str_6)
    assert str_7 == "0<>G!2\t-Z7\tQT&~bjb~&TQ\t7Z-\t2!G><0"
    bool_1 = module_0.is_palindrome(str_4)
    assert bool_1 is False
    str_8 = module_0.make_palindrome(str_4)
    assert str_8 == "#'m`EvhH\n \nHhvE`m'#"
    none_type_0 = None
    str_9 = module_0.make_palindrome(none_type_0)
    assert str_9 == ""
    str_10 = "T<"
    str_11 = module_0.make_palindrome(str_10)
    assert str_11 == "T<T"
    bool_2 = module_0.is_palindrome(str_4)
    assert bool_2 is False