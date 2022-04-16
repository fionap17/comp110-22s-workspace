"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730243735"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes the values attribute of a newly constructed simpy object."""
        self.values = values

    def __str__(self) -> str:
        """Converts a simpy oject into a str representation."""
        return (f"Simpy{self.values}")

    def fill(self, value: float, count: int) -> None:
        """Mutates a given value a given number of times."""
        i: int = 0
        values = []
        self.values = values
        while i < count:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Makes a list of values given a start value, a stop value, and an increment."""
        assert step != 0.0
        values = []
        self.values = values
        while start != stop:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Determines the sum of a list of values."""
        result: float = 0.0
        if len(self.values) != 0:
            result = sum(self.values)
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Creates a new Simpy object by adding either a float value or another Simpy object to the original Simpy object at each of its indices."""
        add_list = []
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for index in range(len(self.values)):
                new_entry = rhs + self.values[index]
                add_list.append(new_entry)
        else:
            assert len(self.values) == len(rhs.values)
            for index in range(len(self.values)):
                new_entry = rhs.values[index] + self.values[index]
                add_list.append(new_entry)
        values = add_list
        result = Simpy(values)
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Creates a new Simpy object by raising either a float value or another Simpy object to the original Simpy object at each of its indices."""
        add_list = []
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for index in range(len(self.values)):
                new_entry = self.values[index] ** rhs
                add_list.append(new_entry)
        else:
            assert len(self.values) == len(rhs.values)
            for index in range(len(self.values)):
                new_entry = self.values[index] ** rhs.values[index]
                add_list.append(new_entry)
        values = add_list
        result = Simpy(values)
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks if values in given Simpy object matches a float value or another simpy object."""
        result: list[bool] = []

        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for index in range(len(self.values)):
                if self.values[index] == rhs.values[index]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Determines whether the Simpy object is greater than a float value or another Simp object."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for index in range(len(self.values)):
                if self.values[index] > rhs.values[index]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows for Simpy object values to be accessed via subscription notation using indices or a bool expression."""
        new_list: list[float] = []
        if isinstance(rhs, int):
            assert rhs < len(self.values)
            for index in range(len(self.values)):
                entry: float = self.values[index]
                new_list.append(entry)
            return new_list[rhs]
        else:
            for index in range(len(rhs)):
                if rhs[index] is True:
                    entry: float = self.values[index]
                    new_list.append(entry)
            result = Simpy(new_list)
            return result