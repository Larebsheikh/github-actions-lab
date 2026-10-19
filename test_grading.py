import pytest
from grading import calculate_grade

def test_grade_a():
    assert calculate_grade(90) == "A"

def test_grade_c():
    assert calculate_grade(60) == "C"

def test_invalid_grade():
    with pytest.raises(ValueError):
        calculate_grade(110)
