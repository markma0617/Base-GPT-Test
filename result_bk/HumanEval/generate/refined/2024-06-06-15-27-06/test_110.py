from code_110 import exchange
def test():
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert exchange([1, 2, 3, 4, 5], [2, 4, 6, 8]) == "YES"