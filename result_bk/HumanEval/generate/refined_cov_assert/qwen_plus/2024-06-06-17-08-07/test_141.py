from code_141 import file_name_check

def test():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example.exe") == 'Yes'
    assert file_name_check("file_name_check.dll") == 'Yes'
    assert file_name_check("123example.txt") == 'No'
    assert file_name_check("abc123.txt") == 'Yes'
    assert file_name_check("text_without_extension") == 'No'
    assert file_name_check(".hidden_file.exe") == 'No'
    assert file_name_check("test123.dll") == 'Yes'
    assert file_name_check("AbC123.dll") == 'No'
