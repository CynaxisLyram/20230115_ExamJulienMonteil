from devine_turing import *
def test_decomposer():
    assert (decomposer(0)) == None
    assert (decomposer(99)) == None
    assert (decomposer(1000)) == None
    assert (decomposer(10000)) == None
    assert (decomposer(100)) == (1,0,0)
    assert (decomposer(555)) == (5,5,5)
    assert (decomposer(999)) == (9,9,9)

def test_divisible():
    assert (divisible(180)) == True
    assert (divisible(200)) == False

def test_somme():
    assert (somme(3,9,6)) == True
    assert (somme(2,5,3)) == True
    assert (somme(3,3,3)) == False
