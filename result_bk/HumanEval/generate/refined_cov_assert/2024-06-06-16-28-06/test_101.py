from code_101 import words_string
def test():
    assert words_string("") == []
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert words_string("Hello World") == ["Hello", "World"]
    assert words_string("This,is,a,test,string") == ["This", "is", "a", "test", "string"]
    assert words_string("1, 2, 3, 4, 5") == ["1", "2", "3", "4", "5"]
    assert words_string("No,spaces,here") == ["No", "spaces", "here"]
    assert words_string("testing,splitting,words") == ["testing", "splitting", "words"]
    assert words_string("Another,example") == ["Another", "example"]
    assert words_string("The,last,one") == ["The", "last", "one"]