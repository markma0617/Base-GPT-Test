from code_157 import right_angle_triangle
def test():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(9, 40, 41) == True
    assert right_angle_triangle(11, 60, 61) == True
    assert right_angle_triangle(13, 84, 85) == True