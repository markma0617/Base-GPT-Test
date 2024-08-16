from code_158 import find_max
def test():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["a", "b", "c", "d"]) == "a"
    assert find_max(["abcd", "efg", "hij"]) == "abcd"
    assert find_max(["apple", "banana", "cherry"]) == "banana"
    assert find_max(["apple", "banana", "cherry", "date"]) == "banana"
    assert find_max(["apple", "banana", "cherry", "date", "elderberry"]) == "elderberry"
    assert find_max(["apple", "banana", "cherry", "date", "elderberry", "fig"]) == "elderberry"
    assert find_max(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]) == "elderberry"