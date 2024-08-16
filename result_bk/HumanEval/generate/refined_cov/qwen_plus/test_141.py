from code_141 import file_name_check

def test():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("valid_name.exe") == 'Yes'
    assert file_name_check("long_number1234.txt") == 'No'
    assert file_name_check(".hiddenfile.dll") == 'No'
    assert file_name_check("test.") == 'No'
    assert file_name_check("test_invalid_extension") == 'No'
