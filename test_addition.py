from addition import add

def test_add_positive():
    assert add(10, 5) == 15

def test_add_negative():
    assert add(-4, -6) == -10
