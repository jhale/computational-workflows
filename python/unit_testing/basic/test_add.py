import pytest
from add import add

@pytest.mark.parametrize("a,b,result", [(3, 5, 8), (-3, -4, -7), (10, -3, 7)])
def test_add(a, b, result):
    c = add(a, b)
    assert(c == result)

def test_add2():
    c = add(20, 10)
    assert(c == 30)
