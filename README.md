# README

## Description

This repo consists of a collection of sorting algorithms for text editing.
Currently, the following sorters are available:

- `lensort`: sort lines of text based on the number of characters before a
  regular expression match is found.

## Installation

You can clone this repo, move to the root directory and run `pip install .` to
install the package.` if you prefer). Use the following single line command to
install the package:

```bash
tmp_dir=$(mktemp -d); git clone https://github.com/BartSte/sorters.git $tmp_dir; pip install $tmp_dir; rm -rf $tmp_dir;
```

or using `pipx` if you prefer to install the package in an isolated
environment:

```bash
tmp_dir=$(mktemp -d); git clone https://github.com/BartSte/sorters.git $tmp_dir; pipx install $tmp_dir; rm -rf $tmp_dir;
```

both commands will clone the repo in a temporary directory, install the package
and remove the temporary directory.

## Usage

### lensort

From the `lensort --help` command:

_Sort lines of text based on the number of characters before a regular
expression match is found. Lines with the least number of characters move to
the top, and lines with the most number of characters move to the bottom. The
text to be sorted is read from stdin and the sorted text is written to
stdout. For example, if we have the following input:_

    abc = 1
    x = 2
    yy = 3

_Then if our regular expression is `=', the output would be:_

    x = 2
    yy = 3
    abc = 1

_If our input was located in a file called `input.txt', we could use the
following command to sort the text when using bash:_

    lensort '=' < input.txt

## Tests

To run the tests, you need to install the `test` dependencies:

```bash
pip install '.[test]'
```

Then move to the root directory and run:

```bash
pytest
```

## Troubleshooting

If you encounter any issues, please report them on the issue tracker at:
[sorters issues](https://github.com/BartSte/sorters/issues)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING](./CONTRIBUTING.md) for
more information.

## License

Distributed under the [MIT License](./LICENCE).
