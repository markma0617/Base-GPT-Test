# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_17 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "'u>Zwz {m;\n/w\x0bL2h"
    module_0.parse_music(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    list_0 = module_0.parse_music(str_0)
    module_0.parse_music(list_0)