from code_141 import file_name_check

def test():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("example") == 'No'
    assert file_name_check("example.tx") == 'No'
    assert file_name_check("example.txxt") == 'No'
    assert file_name_check("example.tx3t") == 'No'
    assert file_name_check("example.exe") == 'Yes'
    assert file_name_check("example.dll") == 'Yes'
    assert file_name_check("example.pdf") == 'No'
