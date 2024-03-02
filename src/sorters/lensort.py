import logging
import re
import sys
from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter
from sys import stdin
from typing import Callable

_DESCRIPTION = """
Sort lines of text based on the number of characters before a regular
expression match is found. Lines with the least number of characters move to
the top, and lines with the most number of characters move to the bottom. The
text to be sorted is read from stdin and the sorted text is written to
stdout. For example, if we have the following input:

    abc = 1
    x = 2
    yy = 3

Then if our regular expression is `=', the output would be:

    x = 2
    yy = 3
    abc = 1

If our input was located in a file called `input.txt', we could use the
following command to sort the text when using bash:

    lensort '=' < input.txt
"""


def main():
    """Entrypoint"""
    try:
        _main()
    except Exception as error:
        logging.error(error)
        sys.exit(1)


def _main():
    """Entrypoint without error handling."""
    parser: ArgumentParser = _make_parser()
    args: Namespace = parser.parse_args()
    logging.basicConfig(level=parser.parse_args().loglevel)

    text: str = _read(args.file) if args.file else stdin.read()
    logging.debug("Input text: %s", text)

    sorted_text: str = lensort(text, args.regex)
    logging.debug("Sorted text: %s", sorted_text)

    print(sorted_text)


def _read(path: str) -> str:
    """
    Read the text from a file.

    Args:
    ----
        path: the path to the file.

    Returns:
    -------
        the text from the file.

    """
    with open(path, "r") as file:
        return file.read()


def _make_parser() -> ArgumentParser:
    """
    Create an argument parser for the lensort command.

    Returns:
    -------
        ArgumentParser: an argument parser for the lensort command.

    """
    parser = ArgumentParser(
        prog="sort_variable_length",
        description=_DESCRIPTION,
        formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument(
        "regex",
        type=str,
        help="The regular expression to sort the text by.")

    parser.add_argument(
        "--loglevel",
        type=str,
        default="INFO",
        help="Set the log level for the program.",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

    parser.add_argument(
        "-f", "--file",
        type=str,
        help=("The file to read the text from. If not provided, text is read "
              "from stdin."))

    return parser


def lensort(lines: str, regex: str) -> str:
    r"""
    Sort the lines based on the number of characters before the regular
    expression match is found. The lines with the least number of characters
    before the regular expression match are moved to the top, and the lines
    with the most number of characters before the regular expression match are
    moved to the bottom. Lines with no match are moved to the top.

    The lines are first sorted based on the total number of characters. This
    ensures that lines with the same number of characters are sorted based on
    their total length.

    Args:
    ----
        lines: lines of text separated by a newline.
        regex: the regular expression

    Returns:
    -------
        sorted variable definitions separated by a newline.

    """
    len_to_match: Callable[[str], int] = make_len_to_match(regex)

    as_list = lines.splitlines()
    as_list.sort(key=len)
    as_list.sort(key=len_to_match)
    return "\n".join(as_list)


def make_len_to_match(regex: str) -> Callable[[str], int]:
    """
    Return a function that takes a line of text and returns the number of
    characters before a meatch with `regex` is found. If no match is found, 0
    is returned.

    Args:
    ----
        regex: the regular expression to match.

    Returns:
    -------
        a function that takes a line of text and returns the number of
        characters before a match with `regex` is found.
    """
    def len_to_match(line: str) -> int:
        match = re.search(regex, line)
        return match.start() if match else 0
    return len_to_match
