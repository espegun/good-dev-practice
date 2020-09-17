# How to pytest

## The purpose
pytest is an alternative to Python's standard unittest module, with far less boilerplate code.

## How does it work?
The tests uses only the plain assert statement, but has a detailed output of which things failed. A test function is any function with a name which starts with "test", like "test_func". The test function contains the assert statements and may or may not be in the same file as the piece of code being tested.

`$ pip install pytest`
```
def inc(x):
    return x + 1

def test_inc():
    assert inc(3) == 5
```

`$ pytest` To run the test(s).<br/>


## Useful commands
`py.test -h` Show help. <br />
`$ pytest` To run the test(s), i.e. all functions `test*` in all files `test_*.py` or `*_test.py`. <br/>
`...`  .... <br />

## Useful links
[Tutorial at guru99](https://www.guru99.com/pytest-tutorial.html)<br/>
[Latest docs](https://docs.pytest.org/en/latest/)<br/>
[Writing test in general](https://docs.python-guide.org/writing/tests/)<br/>
[Pytesting for data science](https://towardsdatascience.com/unit-testing-for-data-scientists-dc5e0cd397fb?source=emailShare-4bc2cf6e09a0-1600340162&_branch_match_id=804235815812269298)<br/>
