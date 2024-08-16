from code_113 import odd_count

def test():
    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3',"11111111"]) == ["the number of odd elements 1n the str1ng 1 of the 1nput.",
                                          "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(['222', '3333', '444444']) == ["the number of odd elements 0n the str0ng 0 of the 0nput.",
                                                   "the number of odd elements 3n the str3ng 3 of the 3nput.",
                                                   "the number of odd elements 0n the str0ng 0 of the 0nput."]
