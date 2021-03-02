import pytest


def test_count():
    assert tuple([1, 2, 3]).count(0) == 0
    assert tuple(range(1, 10, 2)).count(1) == 1
    assert tuple(['a', 'd', 'a']).count('a') == 2


@pytest.mark.parametrize('itereble',
                         [[1, 2, 3], range(1, 10, 2), map(int, ['1', '2', '3']), zip([1, 2, 3], ['a', 'b'])])
def test_init(itereble):
    tuple(itereble)


def test_tuple_immutability():
    with pytest.raises(TypeError):
        a = tuple(1, 2, 3)
        a[0] = 5
