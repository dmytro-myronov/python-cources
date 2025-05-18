# test_math_utils.py

import pytest
from math_utils import divide

def test_divide_correct():
    assert divide(10, 2) == 5.0
    assert divide(-6, 3) == -2.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2.0),
    (5, 2, 2.5),
    (9, -3, -3.0),
    (0, 5, 0.0),
    (-10, -2, 5.0),
])
def test_divide_parametrized(a, b, expected):
    assert divide(a, b) == expected
