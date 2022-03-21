"""Employing dictonaries in different functions: exercise 06."""


__author__ = "730243735"


def invert(inversion: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    inverted_dict: dict[str, str] = dict()
    for key in inversion:
        if inversion[key] in inverted_dict:
            raise KeyError("Duplicated key.")
        else:
            inverted_dict[inversion[key]] = key
    return inverted_dict


def favorite_color(survey: dict[str, str]) -> str:
    """Determines which color is the most popular from a given dictionary."""
    counter: dict[str, int] = {}
    for key in survey:
        if survey[key] in counter:
            counter[survey[key]] += 1
        else:
            counter[survey[key]] = 1
    max: int = 0
    color: str = ""
    for key in counter:
        if counter[key] > max:
            max = counter[key]
            color = key
    return color


def count(characters: list[str]) -> dict[str, int]:
    """Creates a dictionary that keep counts of how many times an item appears in the list."""
    counter: dict[str, int] = {}
    for item in characters:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter