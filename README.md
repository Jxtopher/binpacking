# Bin Packing 2D [![CircleCI](https://circleci.com/gh/Jxtopher/binpacking.svg?style=svg&circle-token=70de38360fc5aa8e02f50443a377512bec444ce1)](https://app.circleci.com/pipelines/github/Jxtopher/binpacking/)



Bin Packing, using optimization to solve the problem!

See <https://en.wikipedia.org/wiki/Bin_packing_problem>

## Requirements

- `git`, this repository must be cloned and commands are to be run from the root directory
- `make`, see <https://www.gnu.org/software/make/>, managed with `Makefile` file
- `pipenv`, see <https://github.com/pypa/pipenv>, managed with `Pipfile` and `Pipfile.lock` files
- `python 3.8`, to be used in a virtual environment with `pipenv` (`pipenv --three` can work)

## Setup

This setup is for development only. Ensure that all requirements are met, especially Docker and that
a virtual environment for Python 3.8 has been created with `pipenv` (`pipenv --three` can work).

Activate the `pipenv` shell environment:

```
make activate
```

Install dependencies:

```
make install
```

Do some plotting:

```
make plot
```

Or run the solver:

```
make run-solver
```

Optionally if you are using VSCode you may use the settings in `.vscode.example/settings.json`:

```sh
cp -r .vscode.example .vscode && echo ".vscode/settings.json" >> .git/info/exclude
```

## Development tools

The codebase is checked for code formatting with `black` (<https://github.com/python/black>),
`mypy` for static typing (<http://mypy-lang.org/>),
and `flake8` for various errors and warnings (<https://pypi.org/project/flake8/>).

_It is strongly recommended to have all of these tools configured within the editor or IDE._

Manual executions of those tools can be done with `make`:

```
# checks:
make flake
make mypy
make black-check

# run all above checks:
make checks

# apply black formatting on the codebase:
make black
```

## Test

Run all tests with:

```
make test
```

Or specific tests with something like:

```
# test a whole file:
make test TARGET=tests.test_directory_1.test_directory_2.test_file

# test a specific test class within a file:
make test TARGET=tests.test_directory_1.test_directory_2.test_file.TestClassName

# test a specific test class method within a file:
make test TARGET=tests.test_directory_1.test_directory_2.test_file.TestClassName.test_method_name
```

For convenience, a file path may also be used (as "/" characters are replaced with "." characters):

```
# test a whole file:
make test TARGET=tests/test_directory_1/test_directory_2/test_file

# test a whole file with ".py" extention also ok as ".py" is removed within the make logic:
make test TARGET=tests/test_directory_1/test_directory_2/test_file.py

# test a specific test class within a file:
make test TARGET=tests/test_directory_1/test_directory_2/test_file.TestClassName

# test a specific test class method within a file:
make test TARGET=tests/test_directory_1/test_directory_2/test_file.TestClassName.test_method_name
```

## Dependencies

Install all dependencies (`pip` packages including development packages) with:

```
make install
```

If new packages are to be added, install them with:

```
make install PACKAGE=new_package_name
```

Or new development packages with:

```
make install DEV_PACKAGE=new_dev_package_name
```

Always commit `Pipfile` and `Pipfile.lock` changes.

Update packages with:

```
make update
```

Or update a single package with:

```
make update PACKAGE=some_package_name
```
