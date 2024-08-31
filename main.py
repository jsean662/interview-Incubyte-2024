import re


class Calculations:

    def handle_empty_input(self, input_data):
        if not input_data:
            return 0
        return None


    def extract_and_update_delimiters(self, input_data):
        delimiters = '\n|,'
        if input_data.startswith('//'):
            input_data = input_data.replace('//', '')
            custom_delimiter = input_data.split('\n')[0]
            delimiters = f'{delimiters}|{custom_delimiter}'
            input_data = '\n'.join(input_data.split('\n')[1:])
        return delimiters, input_data


    def split_input_data(self, input_data, delimiters):
        return re.split(delimiters, input_data)


    def convert_and_sum(self, inputs):
        return sum(int(x) for x in inputs)


    def my_sum(self, input_data):
        # Handle empty input_data
        result = self.handle_empty_input(input_data)
        if result is not None:
            return result
        
        # Extract and update delimiters
        delimiters, input_data = self.extract_and_update_delimiters(input_data)
        
        # Split input data
        inputs = self.split_input_data(input_data, delimiters)
        
        # Convert to integers and sum
        result = self.convert_and_sum(inputs)

        return result
