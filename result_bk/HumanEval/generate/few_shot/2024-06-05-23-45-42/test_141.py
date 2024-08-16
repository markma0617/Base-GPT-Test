from code_141 import file_name_check
def test():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("test.py") == 'No'
    assert file_name_check("file.exe") == 'Yes'
    assert file_name_check("file2.txt") == 'Yes'
    assert file_name_check("file3.dll") == 'Yes'
    assert file_name_check("file4.exe") == 'Yes'
    assert file_name_check("file5.bin") == 'No'