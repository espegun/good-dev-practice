import pytest
import time
from my_program import double_it, bad_double_it, calculate_rectangle_area


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


@pytest.fixture  # Function to run before tests to provide setup data
def get_data():
    input_data = {"side1": 2,
                  "side2": 3}
    return input_data


@pytest.mark.test_using_fixture
def test_calculate_rectangle_area(get_data):

    # Note that the input data has the NAME of the fixture function. Could also be a list instead of dict.
    assert calculate_rectangle_area(get_data["side1"], get_data["side2"]) == 6, "Area calculation failed!"


# Run the same test function with different settings
@pytest.mark.parametrize_test
@pytest.mark.parametrize("input1, output", [(1, 2), (2, 4), (3, 6), (10, 20)])
def test_double_it(input1, output):

    assert double_it(input1) == output, "failed"




