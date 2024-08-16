from code_141 import file_name_check

def test():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("test2.txt") == 'Yes'
    assert file_name_check("abc.exe") == 'Yes'
    assert file_name_check("file123.txt") == 'No'
