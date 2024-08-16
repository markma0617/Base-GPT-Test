from code_103 import rounded_avg

def test():
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(10, 20) == "0b1111"
    assert rounded_avg(20, 33) == "0b11010"
    assert rounded_avg(1, 1) == "0b1"
    assert rounded_avg(2, 2) == "0b1"
    assert rounded_avg(100, 150) == "0b110101"
    assert rounded_avg(50, 60) == "0b1101"
    assert rounded_avg(3, 1) == -1
    assert rounded_avg(99, 101) == "0b110011"
