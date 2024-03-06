import unittest
import pandas as pd
import sys

sys.path.append('../')  # As the task directory is two levels up from unit-test/components

from task.solution import total_revenue_by_product

class TestTotalRevenueByProduct(unittest.TestCase):

    def setUp(self):
        # Sample data with various scenarios
        self.data_empty = pd.DataFrame(columns=['product_name', 'product_price'])

        self.data_single_product = pd.DataFrame({
            'product_name': ['A', 'A', 'A'],
            'product_price': [100, 200, 150]
        })

        self.data_multiple_products = pd.DataFrame({
            'product_name': ['A', 'B', 'C', 'A', 'B', 'C'],
            'product_price': [100, 200, 150, 50, 250, 100]
        })

        self.data_negative_prices = pd.DataFrame({
            'product_name': ['A', 'B', 'C'],
            'product_price': [-100, -200, -150]
        })

    def test_total_revenue_by_product_empty_data(self):
        # When the dataset is empty
        result = total_revenue_by_product(self.data_empty)
        self.assertTrue(result.empty)

    def test_total_revenue_by_product_single_product(self):
        # When the dataset has a single product
        result = total_revenue_by_product(self.data_single_product)
        expected_result = pd.Series([450], index=['A'])
        self.assertTrue(result.equals(expected_result))

    def test_total_revenue_by_product_multiple_products(self):
        # When the dataset has multiple products
        result = total_revenue_by_product(self.data_multiple_products)
        expected_result = pd.Series([150, 450, 250], index=['A', 'B', 'C'])
        self.assertTrue(result.equals(expected_result))

    def test_total_revenue_by_product_negative_prices(self):
        # When the dataset has negative product prices
        result = total_revenue_by_product(self.data_negative_prices)
        expected_result = pd.Series([-100, -200, -150], index=['A', 'B', 'C'])
        self.assertTrue(result.equals(expected_result))

    def test_total_revenue_by_product_duplicate_products(self):
        # When the dataset has duplicate product names
        data = pd.DataFrame({
            'product_name': ['A', 'B', 'C', 'A', 'B', 'C'],
            'product_price': [100, 200, 150, 50, 250, 100]
        })
        result = total_revenue_by_product(data)
        expected_result = pd.Series([150, 450, 250], index=['A', 'B', 'C'])
        self.assertTrue(result.equals(expected_result))

    def test_total_revenue_by_product_no_error(self):
        # When the function executes without errors
        data = pd.DataFrame({
            'product_name': ['A', 'B', 'C'],
            'product_price': [100, 200, 150]
        })
        result = total_revenue_by_product(data)
        self.assertIsNotNone(result)
