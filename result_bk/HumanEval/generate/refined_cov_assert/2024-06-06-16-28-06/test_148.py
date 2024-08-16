from code_148 import bf
def test():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Mars") == ("Earth")
    assert bf("Mars", "Earth") == ("Venus")
    assert bf("Neptune", "Mercury") == ()
    assert bf("Pluto", "Uranus") == ()
    assert bf("Earth", "Earth") == ()
    assert bf("Venus", "Jupiter") == ("Earth", "Mars", "Saturn")
    assert bf("Neptune", "Mercury") == ()