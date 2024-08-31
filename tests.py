import unittest

from main import Calculations


class TestCalculations(unittest.TestCase):

    def test_empty_string(self):
        calc = Calculations()
        assert calc.my_sum("") == 0, (
            "Output should be zero"
        )

    def test_one_number(self):
        calc = Calculations()
        assert calc.my_sum("1") == 1, (
            "Output should be 1"
        )

    def test_two_numbers(self):
        calc = Calculations()
        assert calc.my_sum("1,2") == 3, (
            "Output should be 3"
        )

    def test_three_numbers(self):
        calc = Calculations()
        assert calc.my_sum("1,2,3") == 6, (
            "Output should be 6"
        )

    def test_with_new_line_as_delimiter(self):
        calc = Calculations()
        assert calc.my_sum("1\n2,3") == 6, (
            "Output should be 6"
        )

    def test_with_custom_delimiter(self):
        calc = Calculations()
        assert calc.my_sum(f"//;\n1;3") == 4, (
            "Output should be 6"
        )

    # Test cases for the helper functions
    def test_handle_empty_input(self):
        calc = Calculations()
        assert calc.handle_empty_input("") == 0, "Should return 0 for empty input"
        assert calc.handle_empty_input("1,2") is None, "Should return None for non-empty input"

    def test_extract_and_update_delimiters(self):
        calc = Calculations()
        delimiters, input_data = calc.extract_and_update_delimiters("//;\n1;2")
        assert delimiters == '\n|,|;', "Should include custom delimiter"
        assert input_data == "1;2", "Should remove custom delimiter declaration"

    def test_split_input_data(self):
        calc = Calculations()
        inputs = calc.split_input_data("1,2\n3", '\n|,')
        assert inputs == ['1', '2', '3'], "Should split input data correctly"

    def test_convert_and_sum(self):
        calc = Calculations()
        result = calc.convert_and_sum(['1', '2', '3'])
        assert result == 6, "Should sum the integers correctly"


if __name__ == '__main__':
    unittest.main()
