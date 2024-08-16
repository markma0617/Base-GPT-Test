from code_67 import fruit_distribution

def test():
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19
    assert fruit_distribution("no fruits at all", 5) == 5
    assert fruit_distribution("1 apple and 0 oranges", 3) == 2
