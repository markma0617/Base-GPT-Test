from code_149 import sorted_list_sum

def test():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["xyz", "pq", "lmn"]) == ["pq", "xyz"]
