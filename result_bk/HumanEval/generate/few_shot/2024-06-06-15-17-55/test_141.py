from code_141 import file_name_check

def test():   
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("file_name.dll") == 'Yes'
    assert file_name_check("file_name.txt") == 'Yes'
    assert file_name_check("file_name.exe") == 'Yes'
    assert file_name_check("file_name.ex") == 'No'
    assert file_name_check("file_name.pdf") == 'No'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("file_name.") == 'No'
