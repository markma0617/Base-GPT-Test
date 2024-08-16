from code_149 import sorted_list_sum

def test():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["hello", "world", "python", "test"]) == ["world", "python"]
    assert sorted_list_sum(["a", "bb", "cc", "dd", "ee"]) == ["bb", "cc", "dd"]
    assert sorted_list_sum(["xyz", "abc", "lmn", "pqr"]) == ["abc", "lmn", "pqr"]
    assert sorted_list_sum(["apple", "banana", "orange"]) == ["banana", "orange"]
    assert sorted_list_sum(["cat", "dog", "bird", "fish", "lion", "tiger"]) == ["bird", "lion"]
    assert sorted_list_sum(["python", "java", "c", "ruby"]) == ["java", "python"]
    assert sorted_list_sum(["good", "better", "best"]) == ["best"]
    assert sorted_list_sum(["car", "bus", "bike", "train"]) == ["bike", "train"]
