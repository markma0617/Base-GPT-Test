from code_41 import car_race_collision

def test():
    assert car_race_collision(0) == 0
    assert car_race_collision(1) == 0
    assert car_race_collision(2) == 1
    assert car_race_collision(3) == 3
    assert car_race_collision(4) == 6
