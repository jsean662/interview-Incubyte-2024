import re


def handle_empty_input(input_data):
    if not input_data:
        return 0
    return None

def extract_and_update_delimiters(input_data):
    delimiters = '\n|,'
    if input_data.startswith('//'):
        input_data = input_data.replace('//', '')
        custom_delimiter = input_data.split('\n')[0]
        delimiters = f'{delimiters}|{custom_delimiter}'
        input_data = '\n'.join(input_data.split('\n')[1:])
    return delimiters, input_data


def split_input_data(input_data, delimiters):
    return re.split(delimiters, input_data)


def convert_and_sum(inputs):
    return sum(int(x) for x in inputs)


def my_sum(input_data):
    # Handle empty input_data
    result = handle_empty_input(input_data)
    if result is not None:
        return result
    
    # Extract and update delimiters
    delimiters, input_data = extract_and_update_delimiters(input_data)
    
    # Split input data
    inputs = split_input_data(input_data, delimiters)
    
    # Convert to integers and sum
    result = convert_and_sum(inputs)
    
    print("Result: ", result)
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

def test_with_custom_delimiter(delimiter):
    assert my_sum(f"//{delimiter}\n1{delimiter}3") == 4, (
        "Output should be 6"
    )


if __name__ == "__main__":
    test_empty_string()
    test_one_number()
    test_two_numbers()
    test_three_numbers()
    test_with_new_line_as_delimiter()
    test_with_custom_delimiter(";")
    test_with_custom_delimiter("#")
    test_with_custom_delimiter("@")
    print("All tests passed successfully!!!")
