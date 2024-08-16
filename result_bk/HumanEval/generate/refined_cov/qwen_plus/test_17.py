from code_17 import parse_music

def test():
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o o| o| o| .| .| .|') == [4, 2, 2, 2, 1, 1, 1]
    assert parse_music('o| o| .| .| .| .|') == [2, 2, 1, 1, 1, 1]
