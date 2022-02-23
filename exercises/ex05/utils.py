"""Function skeletons and implementations of exercise 05: lists."""

__author__ = "730243735"


# Name: only_evens
def only_evens(items: list[int]) -> list[int]:
    """Returns all even integers in the list."""
# Arguments: A list of integers.
    x: list[int] = []
    for item in items:
        if item % 2 == 0:
            x.append(item)
            # Returns: A list of integers, containing only the even elements of the input parameter.
    return x


# Name: sub
# Parameters: A list and two ints, where the first int serves as a start index and the second int serves as an end index (not inclusive).
def sub(items: list[int], start: int, end: int) -> list[int]:
    """Returns a subset of integers from a given list. The range is determined by the start and end indexes."""
    new: list[int] = []
    if start < 0:
        start = 0
    if end > len(items):
        end = len(items) - 1
    if len(items) == 0 or start > len(items) or end <= 0:
        return new
    while start < end:
        new.append(items[start])
        start += 1
    # Returns: A List which is a subset of the given list, between the specified start index and the end index - 1.
    return new


# Name: concat
# Parameters: Two lists of ints.
def concat(items_one: list[int], items_two: list[int]) -> list[int]:
    """Generates a new List that contains all of the elements of the first list and all of the elements of the second list."""
# Returns: A list containing all elements of the first list, followed by all elements of the second list.
    items_three: list[int] = []
    for item in items_one:
        items_three.append(item)
    for item in items_two:
        items_three.append(item)
    return items_three