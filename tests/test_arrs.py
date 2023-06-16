import pytest

from utils import arrs


@pytest.fixture
def data():
    return [1, 2, 3, 4, 5]


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice(data, 1, 3) == [2, 3]
    assert arrs.my_slice(data, 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(data, -4, 1) == [1]
    assert arrs.my_slice(data, -1, 10) == [5]
