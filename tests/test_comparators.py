import pytest

from leet.test_suite.comparators import nested_list_comparator


@pytest.mark.parametrize(
    ("l1", "l2", "expected_result"),
    [
        ([[1, 2, 3], [2, 4, 8]], [[4, 2, 8], [3, 1, 2]], True),
        ([[1, 2, 3], [1, 4, 8]], [[4, 2, 8], [3, 1, 2]], False),
    ],
)
def test_nested_list_comparator(l1: list, l2: list, expected_result: bool):
    assert nested_list_comparator(l1=l1, l2=l2) == expected_result
