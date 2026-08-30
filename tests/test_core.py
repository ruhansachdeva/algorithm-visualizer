import pytest
import core

@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 3, 5, 7, 9], 5, 2),       # Target in middle
        ([1, 3, 5, 7, 9], 1, 0),       # Target at start
        ([1, 3, 5, 7, 9], 9, 4),       # Target at end
        ([1, 3, 5, 7, 9], 4, -1),      # Missing target (in-range)
        ([1, 3, 5, 7, 9], 12, -1),     # Missing target (out-of-bounds)
        ([], 5, -1),                   # Empty list
        ([42], 42, 0),                 # Single element found
        ([42], 7, -1),                 # Single element not found
    ]
)
def test_search(arr, target, expected):
    assert core.binary(arr, target) == expected
    assert core.linear(arr, target) == expected

@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1,7,6,4], [1,4,6,7]),       # Even
        ([1, 3, 5, 7, 9], [1,3,5,7,9]),       # Sorted
        ([1], [1]),       # 1 Element
        ([5,3,2,5,6], [2,3,5,5,6]),      # Odd
        ([], []) # Epstein

 
    ]
)
def test_sort(arr, expected):
    assert core.bubble(arr) == expected
    assert core.selection(arr) == expected