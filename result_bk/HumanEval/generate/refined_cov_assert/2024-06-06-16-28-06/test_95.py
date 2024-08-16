from code_95 import check_dict_case

def test():
    assert check_dict_case({}) == False
    assert check_dict_case({"a":"apple", "b":"banana"}) == True
    assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False
    assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False
    assert check_dict_case({"STATE":"NC", "ZIP":"12345"}) == True
