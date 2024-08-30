import re


def my_sum(input_data):
    # Handle empty input_data
    if not input_data:
        return 0
    
    inputs = [int(x) for x in re.split(',|\n', input_data)]

    result = sum(inputs)
    # print("Result: ", result)

    return result



def test_empty_string():
    assert my_sum("") == 0, (
        "Output should be zero"
    )

def test_one_number():
    assert my_sum("1") == 1, (
        "Output should be 1"
    )

def test_two_numbers():
    assert my_sum("1,2") == 3, (
        "Output should be 3"
    )

def test_three_numbers():
    assert my_sum("1,2,3") == 6, (
        "Output should be 6"
    )

def test_with_new_line_as_delimiter():
    assert my_sum("1\n2,3") == 6, (
        "Output should be 6"
    )


if __name__ == "__main__":
    test_empty_string()
    test_one_number()
    test_two_numbers()
    test_three_numbers()
    test_with_new_line_as_delimiter()
    print("All tests passed successfully!!!")
