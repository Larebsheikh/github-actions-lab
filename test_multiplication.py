from multiplication import multiply

def test_multiply_integers():
    assert multiply(4, 5) == 20

def test_multiply_zero():
    assert multiply(8, 0) == 0
