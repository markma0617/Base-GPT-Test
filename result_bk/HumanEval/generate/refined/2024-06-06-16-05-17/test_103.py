from code_103 import rounded_avg

def test():   
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(10, 20) == "0b1111"
    assert rounded_avg(20, 33) == "0b11010"
