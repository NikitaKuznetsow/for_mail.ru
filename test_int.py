import pytest
from hypothesis import given, strategies as st


@pytest.mark.parametrize('int1', [-10, 0, 10])
@pytest.mark.parametrize('int2', [-10, 0, 10])
def test_commutability(int1, int2):
    assert int(int1) + int(int2) == int(int2) + int(int1)


def test_init_error():
    with pytest.raises(ValueError):
        int('a')
    with pytest.raises(TypeError):
        int([1, 2, 3])


@given(st.integers(), st.integers())
def test_multiply(int1, int2):
    assert int(int1) * int(int2) == int(int1 * int2)

