from __future__ import annotations


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: str) -> StrArray: 
        """Vectorized concatenation operator."""
        # Setup a result list of strings thts empy
        result: list[str] = []
        # Loop through each item in self.item
        for item in self.items:
            # For each item, append the concatenation of item and rhs to result list
            result.append(item + rhs)
        # Return a newly constructed StrArray whose items are result
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!!!"
print(result)
# print(first + last)
