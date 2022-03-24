"""Dictionary related utility functions."""

__author__ = "730243735"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads entire CSV and puts into a table."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = dict()
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], count: int) -> dict[str, list[str]]:
    """Produces a column-oriented table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if count >= len(table):
        result = table
        return result 
    for column in table:
        new_list: list[str] = []
        for index in range(count):
            new_list.append(table[column][index])
        result[column] = new_list
    return result


def select(table: dict[str, list[str]], name_of_column: list[str]) -> dict[str, list[str]]:
    """Produces a table of a subset of the original columns."""
    sub_dict: dict[str, list[str]] = {}

    for name in name_of_column:
        if name in table:
            sub_dict[name] = table[name]
    return sub_dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-oriented tables into one."""
    combined_table: dict[str, list[str]] = {}

    for key in table_1:
        combined_table[key] = table_1[key]
    for key in table_2:
        if key in combined_table:
            combined_table[key] = table_1[key] + table_2[key]
        else:
            combined_table[key] = table_2[key]
    return combined_table


def count(char_to_count: list[str]) -> dict[str, int]:
    """Produces a dict[str, int] that counts the number of times values from a list[str] occurs."""
    new_dict: dict[str, int] = {}
    
    for character in char_to_count:
        if character in new_dict:
            new_dict[character] += 1
        else:
            new_dict[character] = 1
    return new_dict