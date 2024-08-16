from code_158 import find_max

def test():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["hello", "world", "example"]) == "hello"
    assert find_max(["abcde", "bcdea", "cdeab"]) == "abcde"
    assert find_max(["xyzzzz", "zxx", "zzzxy"]) == "xyzzzz"
    assert find_max(["sameunique", "unique", "same"]) == "unique"
    assert find_max(["aaaaa", "bb", "ccc"]) == "ccc"
    assert find_max(["abcdefg", "ghijklmn", "pqrstuvwxy"]) == "abcdefg"
    assert find_max(["python", "java", "javascript"]) == "python"
