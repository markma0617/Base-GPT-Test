from code_103 import rounded_avg

def test():
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(10, 20) == "0b1111"
    assert rounded_avg(20, 33) == "0b11010"
    assert rounded_avg(5, 5) == "0b101"
    assert rounded_avg(3, 3) == "0b11"
    assert rounded_avg(10, 10) == "0b1010"
    assert rounded_avg(20, 20) == "0b10100"
    assert rounded_avg(1, 10) == "0b1010"
    assert rounded_avg(1, 1) == "0b1"
