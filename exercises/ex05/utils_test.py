"""Tests for utils functions."""

__author__ = "730243735"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests edge case of an empty list for only_evens function.""" 
    items: list[int] = []
    assert only_evens(items) == []


def test_only_evens_no_evens() -> None:
    """Tests use case of no even integers in list."""
    items: list[int] = [1, 3, 5, 7]
    assert only_evens(items) == []


def test_only_evens_mixed() -> None:
    """Tests use case of both odd and even integers in list."""
    items: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(items) == [2, 4]


def test_sub_empty() -> None:
    """Tests edge case of an empty list for sub function."""
    items: list[int] = []
    start: int = 1
    end: int = 2
    assert sub(items, start, end) == []


def test_sub_single_item() -> None:
    """Tests edge case of a list with only one item."""
    items: list[int] = [3]
    start: int = 0
    end: int = 1
    assert sub(items, start, end) == [3]


def test_sub_single_item_end() -> None:
    """Tests edge case of a list with only one item. Start and end index are the same."""
    items: list[int] = [3]
    start: int = 2
    end: int = 2
    assert sub(items, start, end) == []


def test_sub_end_greater_than_length() -> None:
    """Tests use case when end index is greater than length of list."""
    items: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    start: int = 3
    end: int = 12
    assert sub(items, start, end) == [4, 5, 6, 7]


def test_sub_start_equal_length() -> None:
    """Tests sub when start index is the length of the list."""
    items: list[int] = [3]
    start: int = 1
    end: int = 3
    assert sub(items, start, end) == []


def test_sub_in_range() -> None:
    """Tests use case of a list of integers for sub function."""
    items: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = 1
    end: int = 4
    assert sub(items, start, end) == [2, 3, 4]


def test_sub_index_out_range() -> None:
    """Tests use case of sub when start and end integers are out of range of list length."""
    items: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = -2
    end: int = 12
    assert sub(items, start, end) == [1, 2, 3, 4, 5]


def test_concat_two_empty() -> None:
    """Tests edge case of two empty lists for concat function."""
    items_one: list[int] = []
    items_two: list[int] = []
    assert concat(items_one, items_two) == []


def test_concat_one_empty() -> None:
    """Tests edge case of one list is empty for concat function."""
    items_one: list[int] = []
    items_two: list[int] = [1, 2, 3, 4]
    assert concat(items_one, items_two) == [1, 2, 3, 4]


def test_concat_two_normal() -> None:
    """Tests use case of two lists of integers."""
    items_one: list[int] = [1, 2, 3, 4]
    items_two: list[int] = [1, 2, 3, 4]
    assert concat(items_one, items_two) == [1, 2, 3, 4, 1, 2, 3, 4]


def test_concat_mix_list_length() -> None:
    """Tests use case of two lists of integers with different list lengths."""
    items_one: list[int] = [1, 2]
    items_two: list[int] = [1, 2, 3, 4]
    assert concat(items_one, items_two) == [1, 2, 1, 2, 3, 4]