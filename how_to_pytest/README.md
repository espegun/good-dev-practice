# How to pytest

## The purpose
pytest is an alternative to Python's standard unittest module, with far less boilerplate code.

## How does it work?
The tests uses only the plain assert statement, but has a detailed output of which things failed. A test function is any function with a name which starts with "test", like "test_func". The test function contains the assert statements and may or may not be in the same file as the piece of code being tested.

A test in it's simplest form, go more into detail in the attached `.py` files in the repo.
```
def inc(x):
    return x + 1

def test_inc():
    assert inc(3) == 4
```
Test functions may be given marks (wrappers)
```
@pytest.mark.skip  # Always skip it.
def test_func1():

@pytest.mark.my_custom_mark
def test func2():
```
Custom marks should be defined in the `pytest.ini` file.
```
[pytest]
markers =
    my_custom_mark1: One group of tests.
    my_custom_mark2: Another group of tests.
```

## Useful commands
`$ pip install pytest` Install from PyPI. <br/>
`$ pytest -h` Show help.<br/>
`$ pytest` To run the test(s), i.e. all functions `test*` in all files `test_*.py` or `*_test.py`. <br/>
`$ pytest filename` Run only the tests in this file.<br/>
`$ pytest -k string` Run only a subset of test functions. The `string` must match a part of the test function name for it to run.<br/>
`$ pytest -m my_custom_mark` Run one those marked with this mark. This requires `import pytest` in the test file.<br/>
`$ pytest -m "not my_custom_mar<k"` Run everything except those marked with this mark.<br/>
`$ ...` ....<br/>
`$ ...` ....<br/>

## Useful links
[Tutorial at guru99](https://www.guru99.com/pytest-tutorial.html)<br/>
[Latest docs](https://docs.pytest.org/en/latest/)<br/>
[Writing test in general](https://docs.python-guide.org/writing/tests/)<br/>
[Pytesting for data science](https://towardsdatascience.com/unit-testing-for-data-scientists-dc5e0cd397fb?source=emailShare-4bc2cf6e09a0-1600340162&_branch_match_id=804235815812269298)<br/>
