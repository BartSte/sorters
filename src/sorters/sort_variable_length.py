#!/usr/bin/env python3

from argparse import ArgumentParser
from sys import stdin

_DESCRIPTION = """
Sort variable definitions based on the number of characters before the `='. If no `=' is found,
the line length is used. The text to be sorted is read from stdin and the sorted text is written to
stdout. No further arguments are required."""


def sort_variable_length(lines: str) -> str:
    r"""
    First sort all lines based on their total length. Next, sort the lines
    based on the number of characters before the `=' sign. If no equal sign is
    found, the line is ignored.

    Args:
    ----
        lines (str): variable definitions separated by `\n'.

    Returns:
    -------
        str: sorted variable definitions separated by `\n'.

    """
    as_list = lines.splitlines()
    as_list.sort(key=len)
    as_list.sort(key=find_equal_sign)
    return "\n".join(as_list)


def find_equal_sign(obj: str) -> int:
    """
    Return the index of the first `=' sign.

    Args:
    ----
        obj: a string that may contain an `=' sign.

    Returns:
    -------
        int: the location of the first `=' sign.

    """
    return obj.find("=")


def main():
    """Entrypoint"""
    parser = ArgumentParser(
        prog="sort_variable_length",
        description=_DESCRIPTION,
    )
    parser.parse_args()
    print(sort_variable_length(stdin.read()))


if __name__ == "__main__":
    main()