from code_17 import parse_music

def test():
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o| o| .| .|') == [2, 2, 1, 1]
    assert parse_music('o o o') == [4, 4, 4]
    assert parse_music('.| .| .|') == [1, 1, 1]
    assert parse_music('o| o| o| o|') == [2, 2, 2, 2]
    assert parse_music('') == []
    assert parse_music('o o| invalid') == [4, 2]
    assert parse_music('o| o| .||') == [2, 2, 1]
    assert parse_music('o o| .| .| extra_data') == [4, 2, 1, 1]
    assert parse_music('o o| .| .|    o o') == [4, 2, 1, 1, 4, 4]
