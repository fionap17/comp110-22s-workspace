"""Examples of function that searches through a list."""


# Define a function named contains
# Two parameters:
# 1. needle - string we're searching for
# 2. haystack - the list we're search through
def contains(needle: str, haystack: list[str]) -> bool:
    
    # Algorithm:
    # for each item in hay stack
    #   Test if it is equal to the needle
    #       if so, return True
    for item in haystack:
        if item == needle:
            return True
    # After testing all items, return False, because not found
    # Returns true if needle in haystack, false otherwise
    return False
