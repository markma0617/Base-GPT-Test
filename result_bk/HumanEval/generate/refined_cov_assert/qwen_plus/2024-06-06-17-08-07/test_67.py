from code_67 import fruit_distribution

def test():
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19
    assert fruit_distribution("1 apple and 1 orange", 3) == 1
    assert fruit_distribution("no apples and 7 oranges", 7) == 0
    assert fruit_distribution("999 apples and 0 oranges", 1000) == 1
    assert fruit_distribution("10 apples and 20 oranges", 50) == 10
    assert fruit_distribution("200 apples and 50 oranges", 300) == 50
    assert fruit_distribution("1000 apples and 500 oranges", 2000) == 500
