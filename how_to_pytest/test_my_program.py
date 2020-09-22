import pytest
import time
from my_program import double_it, bad_double_it


@pytest.mark.main_test
def test_double_it():

    """Will execute, since the function name starts with 'test'."""

    assert double_it(5) == 10
    assert double_it(6) == 14  # The problem where is of course the expectation, not the tested function.
    assert double_it(0) == 52  # Never executed, this function is left immediately after the above fail.


@pytest.mark.main_test
def test_bad_double_it_description():
    """Get descriptive output."""

    parameter = 10 
    expected = 20
    result = bad_double_it(parameter)
    assert result == expected, f"Failed because {result} != {expected}."


@pytest.mark.slow_test
def test_pass():
    time.sleep(1)
    assert True


@pytest.mark.skip  # Always skip it.
def test_really_slow():
    print("Oh, dear! I thought we agreed to skip this test?")
    time.sleep(5)
    assert False



