from code_152 import compare
def test():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]
    assert compare([10,20,30,40,50],[10,25,30,45,50]) == [0,5,0,5,0]