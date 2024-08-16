from code_141 import file_name_check

def test():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("test1234.exe") == 'No'
    assert file_name_check(".dll") == 'No'
