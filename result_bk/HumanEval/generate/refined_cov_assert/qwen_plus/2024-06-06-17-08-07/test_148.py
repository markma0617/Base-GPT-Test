from code_148 import bf

def test():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Neptune", "Mercury") == ()
    assert bf("Earth", "Mars") == ("Venus")
    assert bf("Jupiter", "Jupiter") == ()
    assert bf("Saturn", "Mercury") == ("Venus", "Earth", "Mars")
    assert bf("Mercury", "Saturn") == ("Venus", "Earth", "Mars", "Jupiter")
    assert bf("Uranus", "Earth") == ("Venus")
    assert bf("Mars", "Jupiter") == ("Venus", "Earth")
