from code_113 import odd_count

def test():
    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3',"11111111"]) == ["the number of odd elements 1n the str1ng 1 of the 1nput.",
                                           "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(['2468', '1357']) == ["the number of odd elements 2n the str2ng 2 of the 2nput.",
                                           "the number of odd elements 4n the str4ng 4 of the 4nput."]
