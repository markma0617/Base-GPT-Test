from code_95 import check_dict_case

def test():
    assert check_dict_case({"a": "apple", "b": "banana"}) == True
    assert check_dict_case({"a": "apple", "A": "banana", "B": "banana"}) == False
    assert check_dict_case({"a": "apple", 8: "banana", "a": "apple"}) == False
    assert check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) == False
    assert check_dict_case({"STATE": "NC", "ZIP": "12345"}) == True
    assert check_dict_case({}) == False
    assert check_dict_case({"ABC": "abc", "DEF": "def"}) == True
    assert check_dict_case({"abc": "abc", "def": "def"}) == True
    assert check_dict_case({"Abc": "abc", "Def": "def"}) == False
    assert check_dict_case({"123": "abc", "456": "def"}) == False
