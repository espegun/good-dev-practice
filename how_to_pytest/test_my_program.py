from my_program import double_it

def test_double_it():
    "Will execute, since the function name starts with 'test'."
    assert double_it(5) == 10
    assert double_it(6) == 14
    assert double_it(0) == 52  # Never executed, this function is left immediately after the above fail. 

def test_double_it_description():
    "Get descriptive output."
    parameter = 10 
    expected = (parameter * 2) + 0.05
    result = double_it(parameter)
    assert double_it(parameter) == expected, f"Failed because {result} != {expected}."



