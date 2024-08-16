from code_149 import sorted_list_sum

def test():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["bcd", "efg", "hij", "klm"]) == ["bcd", "klm"]
    assert sorted_list_sum(["xy", "pq", "ab", "cd"]) == ["ab"]
    assert sorted_list_sum(["apple", "banana", "orange", "kiwi"]) == ["apple", "banana"]
