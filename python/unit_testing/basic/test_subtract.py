import pytest
from subtract import subtract

def test_subtract():
    c = subtract(4, 5)
    assert(c == -1)

def test_subtract_error():
    with pytest.raises(TypeError):
        c = subtract(4, "b")
