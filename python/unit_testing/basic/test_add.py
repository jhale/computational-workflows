import pytest
from add import add

def test_add():
    c = add(4, 6)
    assert(c == 10)

