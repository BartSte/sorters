import logging
import sys
from argparse import ArgumentParser
from sys import stdin

_DESCRIPTION = """
Sort variable definitions based on the number of characters before the `='. If no `=' is found,
the line length is used. The text to be sorted is read from stdin and the sorted text is written to
stdout. No further arguments are required."""


def main():
    """Entrypoint"""
    try:
        _main()
    except BaseException as error:
        logging.error(error)
        sys.exit(1)


def _main():
    """Entrypoint without error handling."""
    parser: ArgumentParser = make_parser()
    parser.parse_args()
    logging.basicConfig(level=parser.parse_args().loglevel)

    text: str = stdin.read()
    logging.debug("Input text: %s", text)

    sorted_text: str = sort_variable_length(text)
    logging.debug("Sorted text: %s", sorted_text)

    print(sorted_text)


def make_parser() -> ArgumentParser:
    """
    Create an argument parser for the lensort command.

    Returns:
    -------
        ArgumentParser: an argument parser for the lensort command.

    """
    parser = ArgumentParser(
        prog="sort_variable_length",
        description=_DESCRIPTION)
    parser.add_argument(
        "--loglevel",
        type=str,
        default="INFO",
        help="Set the log level for the program.",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    return parser


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
