import unittest
import pandas as pd
import sys

sys.path.append('../')  # As the task directory is two levels up from unit-test/components

from task.solution import read_data

class TestReadData(unittest.TestCase):

    def test_read_data_file_found(self):
        # When the file is found and read successfully
        file_path = 'test_data.csv'
        data = pd.DataFrame({
            'order_date': ['2022-01-01', '2022-01-05', '2022-01-10'],
            'product_price': [100, 200, 150]
        })
        data.to_csv(file_path, index=False)
        result = read_data(file_path)
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertEqual(len(result), len(data))
        self.assertTrue(all(result.columns == data.columns))
        # Clean up
        import os
        os.remove(file_path)

    def test_read_data_file_not_found(self):
        # When the file is not found
        file_path = 'non_existent_file.csv'
        result = read_data(file_path)
        self.assertIsNone(result)

    def test_read_data_empty_file(self):
        # When the file is empty
        file_path = 'empty_data.csv'
        open(file_path, 'a').close()
        result = read_data(file_path)
        self.assertIsNone(result)
        # Clean up
        import os
        os.remove(file_path)

    def test_read_data_invalid_file(self):
        # When the file is not a valid CSV file
        file_path = 'invalid_data.txt'
        with open(file_path, 'w') as f:
            f.write("This is not a CSV file.")
        result = read_data(file_path)
        self.assertIsNone(result)
        # Clean up
        import os
        os.remove(file_path)

    def test_read_data_exception(self):
        # When an exception occurs during file reading
        file_path = 'test_data.csv'
        with open(file_path, 'w') as f:
            f.write("This is a corrupted CSV file.")
        result = read_data(file_path)
        self.assertIsNone(result)
        # Clean up
        import os
        os.remove(file_path)
