from code_157 import right_angle_triangle

def test():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(6, 8, 10) == True
    assert right_angle_triangle(9, 12, 15) == True
    assert right_angle_triangle(4, 5, 7) == False
    assert right_angle_triangle(10, 20, 26) == False
    assert right_angle_triangle(1, 1, 2) == False
    assert right_angle_triangle(0, 0, 0) == False
