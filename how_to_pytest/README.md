# How to pytest

## The purpose
pytest is an alternative to Python's standard unittest module, with far less boilerplate code.

## How does it work?
The tests uses only the plain assert statement, but has a detailed output of which things failed. A test function is any function with a name which starts with "test", like "test_func". The test function contains the assert statements and may or may not be in the same file as the piece of code being tested.

`$ pip install pytest`
```
$ pytest

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```


## Useful commands
`...`  .... <br />
`...`  .... <br />

## Useful links
[Tutorial at guru99](https://www.guru99.com/pytest-tutorial.html)<br/>
[Latest docs](https://docs.pytest.org/en/latest/)<br/>
[Writing test in general](https://docs.python-guide.org/writing/tests/)<br/>
