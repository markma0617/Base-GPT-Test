from code_157 import right_angle_triangle
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(20, 21, 29) == True