# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import code_2 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x030U\xad\xed\xb8\xb6\xd7|\x0e \x84\xbb\x06="
    module_0.truncate_number(bytes_0)
