from code_110 import exchange
def test():
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert exchange([2, 4, 6, 8], [1, 2, 3, 4]) == "YES"
    assert exchange([1, 3, 5, 7], [0, 2, 4, 6]) == "NO"
    assert exchange([1, 1, 1], [2, 2, 2]) == "YES"