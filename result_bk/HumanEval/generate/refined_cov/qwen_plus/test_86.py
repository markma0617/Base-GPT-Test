from code_86 import anti_shuffle

def test():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    assert anti_shuffle("Python Programming") == "PyhnrnoPgimmtio"
    assert anti_shuffle("A quick brown dog jumps over the lazy fox") == "A bcdejklmnooppqrtuvwx fox lazy over jumps qruvwxy"
