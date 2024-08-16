from code_41 import car_race_collision

def test():
    assert car_race_collision(0) == 0
    assert car_race_collision(1) == 1
    assert car_race_collision(2) == 4
    assert car_race_collision(3) == 9
    assert car_race_collision(5) == 25
    assert car_race_collision(10) == 100
    assert car_race_collision(100) == 10000
    assert car_race_collision(-1) == 1
    assert car_race_collision(-5) == 25
    assert car_race_collision(-10) == 100
