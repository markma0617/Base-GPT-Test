from code_157 import right_angle_triangle
def test():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(1, 2, 3) == False