import unittest
import pandas as pd
import sys

sys.path.append('../')  # As the task directory is two levels up from unit-test/components

from task.solution import total_revenue_by_customer


class TestTotalRevenueByCustomer(unittest.TestCase):

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

        self.data_duplicate_customers = pd.DataFrame({
            'customer_id': [1, 2, 3, 1, 2, 3],
            'product_price': [100, 200, 150, 50, 250, 100]
        })

        self.data_negative_product_prices = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'product_price': [-100, -200, -150]
        })

        self.data_increasing_product_prices = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'product_price': [100, 200, 300]
        })

    def test_total_revenue_by_customer_less_than_10(self):
        # When the dataset has less than 10 customers
        result = total_revenue_by_customer(self.data_less_than_10_customers)
        self.assertEqual(len(result), len(self.data_less_than_10_customers))
        self.assertTrue(all(result.index.isin(self.data_less_than_10_customers['customer_id'])))

    def test_total_revenue_by_customer_more_than_10(self):
        # When the dataset has more than 10 customers
        result = total_revenue_by_customer(self.data_more_than_10_customers)
        self.assertEqual(len(result), 11)  # 11 unique customers
        self.assertTrue(all(result.index.isin(self.data_more_than_10_customers['customer_id'])))

    def test_total_revenue_by_customer_empty_data(self):
        # When the dataset is empty
        result = total_revenue_by_customer(self.empty_data)
        self.assertTrue(result.empty)

    def test_total_revenue_by_customer_duplicate_customers(self):
        # When the dataset has duplicate customer IDs
        result = total_revenue_by_customer(self.data_duplicate_customers)
        self.assertEqual(len(result), 3)  # Only 3 unique customers
        self.assertTrue(all(result.index.isin(self.data_duplicate_customers['customer_id'])))
        self.assertEqual(result[1], 150)  # Sum of product prices for customer 1

    def test_total_revenue_by_customer_negative_product_prices(self):
        # When the dataset has negative product prices
        result = total_revenue_by_customer(self.data_negative_product_prices)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(result.index.isin(self.data_negative_product_prices['customer_id'])))
        self.assertEqual(result[1], -100)  # Sum of negative product prices for customer 1

    def test_total_revenue_by_customer_increasing_product_prices(self):
        # When the dataset has increasing product prices
        result = total_revenue_by_customer(self.data_increasing_product_prices)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(result.index.isin(self.data_increasing_product_prices['customer_id'])))
        self.assertEqual(result[1], 100)  # Sum of increasing product prices for customer 1

