
def my_sum(input_data):
    pass


def test_empty_string():
    assert my_sum("") == 0, (
        "Output should be zero"
    )

def test_one_number():
    assert my_sum("1") == 1, (
        "Output should be 1"
    )


if __name__ == "__main__":
    test_empty_string()
    # test_one_number()
    print("All tests passed successfully!!!")