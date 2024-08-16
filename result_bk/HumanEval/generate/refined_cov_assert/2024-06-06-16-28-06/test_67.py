from code_67 import fruit_distribution

def test():
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19
    assert fruit_distribution("10 apples and 20 oranges", 50) == 20
    assert fruit_distribution("15 apples and 8 oranges", 30) == 7
    assert fruit_distribution("3 apples and 5 oranges", 15) == 7
    assert fruit_distribution("1 apples and 1 oranges", 5) == 3
    assert fruit_distribution("7 apples and 4 oranges", 10) == -1
    assert fruit_distribution("0 apples and 0 oranges", 0) == 0
