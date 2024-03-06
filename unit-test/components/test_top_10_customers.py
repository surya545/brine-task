import unittest
import pandas as pd
import sys

sys.path.append('../')  # As the task directory is two levels up from unit-test/components

from task.solution import top_10_customers


class TestTop10Customers(unittest.TestCase):

    def setUp(self):
        # Sample data with various scenarios
        self.data_less_than_10_customers = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'product_price': [100, 200, 150]
        })

        self.data_more_than_10_customers = pd.DataFrame({
            'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            'product_price': [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550]
        })

        self.empty_data = pd.DataFrame(columns=['customer_id', 'product_price'])

    def test_top_10_customers_less_than_10(self):
        # When the dataset has less than 10 customers
        result = top_10_customers(self.data_less_than_10_customers)
        self.assertEqual(len(result), len(self.data_less_than_10_customers))
        self.assertTrue(all(result.index.isin(self.data_less_than_10_customers['customer_id'])))

    def test_top_10_customers_more_than_10(self):
        # When the dataset has more than 10 customers
        result = top_10_customers(self.data_more_than_10_customers)
        self.assertEqual(len(result), 10)
        self.assertTrue(all(result.index.isin(self.data_more_than_10_customers['customer_id'])))
        self.assertTrue(all(result.iloc[i] >= result.iloc[i+1] for i in range(len(result)-1)))

    def test_top_10_customers_empty_data(self):
        # When the dataset is empty
        result = top_10_customers(self.empty_data)
        self.assertTrue(result.empty)

    def test_top_10_customers_duplicate_customers(self):
        # When the dataset has duplicate customer IDs
        data = pd.DataFrame({
            'customer_id': [1, 2, 3, 1, 2, 3],
            'product_price': [100, 200, 150, 50, 250, 100]
        })
        result = top_10_customers(data)
        self.assertEqual(len(result), 3)  # Only 3 unique customers
        self.assertTrue(all(result.index.isin(data['customer_id'])))

    def test_top_10_customers_negative_product_prices(self):
        # When the dataset has negative product prices
        data = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'product_price': [-100, -200, -150]
        })
        result = top_10_customers(data)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(result.index.isin(data['customer_id'])))

    def test_top_10_customers_increasing_product_prices(self):
        # When the dataset has increasing product prices
        data = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'product_price': [100, 200, 300]
        })
        result = top_10_customers(data)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(result.index.isin(data['customer_id'])))

