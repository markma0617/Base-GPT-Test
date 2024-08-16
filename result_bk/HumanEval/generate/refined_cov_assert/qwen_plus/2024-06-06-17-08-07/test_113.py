from code_113 import odd_count

def test():
    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3', "11111111"]) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(['000', '1234', '55555']) == ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 2n the str2ng 2 of the 2nput.", "the number of odd elements 5n the str5ng 5 of the 5nput."]
    assert odd_count(['1', '22', '333', '4444']) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 3n the str3ng 3 of the 3nput.", "the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['1010', '202020']) == ["the number of odd elements 2n the str2ng 2 of the 2nput.", "the number of odd elements 2n the str2ng 2 of the 2nput."]
