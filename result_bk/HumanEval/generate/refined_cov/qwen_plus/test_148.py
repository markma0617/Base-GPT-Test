from code_148 import bf

def test():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Uranus", "Mercury") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
