"""Tests for my dictionaries in exercises 06."""


__author__ = "730243735"

from exercises.ex06 import dictionary


def test_invert() -> None:
    """Test use case of invert function when given unique key-value pairs."""
    test_dict: dict[str, str] = {"A": "a", "B": "b", "C": "c", "D": "d"}
    assert dictionary.invert(test_dict) == {"a": "A", "b": "B", "c": "C", "d": "D"}


def test_invert_empty_dict() -> None:
    """Test edge case use of empty dictionary on invert function."""
    test_dict: dict[str, str] = {}
    assert dictionary.invert(test_dict) == {}


def test_invert_words_and_characters() -> None:
    """Tests use case of dictionary with both words and characters on invert function."""
    test_dict: dict[str, str] = {"cats": "dogs", "1": "three", "away": "trial", "T": "d"}
    assert dictionary.invert(test_dict) == {"dogs": "cats", "three": "1", "trial": "away", "d": "T"}


def test_favorite_color_no_fav() -> None:
    """Tests edge case of favorite_color function: all colors are equal in favor."""
    survey: dict[str, str] = {"ty": "blue", "chey": "orange", "fi": 'pink', "alex": "grey"}
    assert dictionary.favorite_color(survey) == "blue"


def test_favorite_color_two_fav() -> None:
    """Tests use case of favorite_color function: two colors are equal in favor."""
    survey: dict[str, str] = {"ty": "blue", "chey": "pink", "fi": 'blue', "alex": "pink"}
    assert dictionary.favorite_color(survey) == "blue"


def test_favorite_color() -> None:
    """Tests use case of favorite_color function: one favorite color."""
    survey: dict[str, str] = {"ty": "blue", "chey": "orange", "fi": 'pink', "alex": "pink"}
    assert dictionary.favorite_color(survey) == "pink"


def test_count() -> None:
    """Test use case of count function: list of words, both unique and repeated."""
    sentence: list[str] = ["the", "cat", "and", "the", "dog", "are", "friends"]
    assert dictionary.count(sentence) == {"the": 2, "cat": 1, "and": 1, "dog": 1, "are": 1, "friends": 1}


def test_count_no_repeats() -> None:
    """Test edge case of count function: all unique items in list."""
    sentence: list[str] = ["the", "cat", "and", "mouse", "dog", "are", "friends"]
    assert dictionary.count(sentence) == {"the": 1, "cat": 1, "and": 1, "mouse": 1, "dog": 1, "are": 1, "friends": 1}


def test_count_various_counts() -> None:
    """Test use case of count function: a variety of different counts."""
    sentence: list[str] = ["the", "cat", "and", "the", "dog", "are", "friends", "dog", "cat", "the", "cat", "the"]
    assert dictionary.count(sentence) == {"the": 4, "cat": 3, "and": 1, "dog": 2, "are": 1, "friends": 1}