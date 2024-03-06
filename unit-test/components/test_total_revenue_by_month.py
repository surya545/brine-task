import unittest
import pandas as pd
import sys

sys.path.append('../')  # As the task directory is two levels up from unit-test/components

from task.solution import total_revenue_by_month

class TestTotalRevenueByMonth(unittest.TestCase):

    def setUp(self):
        # Sample data with various scenarios
        self.data_empty = pd.DataFrame(columns=['order_date', 'product_price'])

        self.data_single_month = pd.DataFrame({
            'order_date': ['2022-01-01', '2022-01-05', '2022-01-10'],
            'product_price': [100, 200, 150]
        })

        self.data_multiple_months = pd.DataFrame({
            'order_date': ['2022-01-01', '2022-01-05', '2022-02-10', '2022-02-15', '2022-03-20'],
            'product_price': [100, 200, 150, 50, 250]
        })

        self.data_invalid_date = pd.DataFrame({
            'order_date': ['2022-01-01', 'invalid_date', '2022-01-10'],
            'product_price': [100, 200, 150]
        })

    def test_total_revenue_by_month_empty_data(self):
        # When the dataset is empty
        result = total_revenue_by_month(self.data_empty)
        self.assertTrue(result.empty)

    def test_total_revenue_by_month_single_month(self):
        # When the dataset has data for a single month
        result = total_revenue_by_month(self.data_single_month)
        expected_result = pd.Series([450], index=pd.PeriodIndex(['2022-01'], freq='M'))
        self.assertTrue(result.equals(expected_result))

    def test_total_revenue_by_month_invalid_date(self):
        # When the dataset has invalid date
        with self.assertRaises(ValueError):
            total_revenue_by_month(self.data_invalid_date)

    def test_total_revenue_by_month_no_error(self):
        # When the function executes without errors
        data = pd.DataFrame({
            'order_date': ['2022-01-01', '2022-01-05', '2022-01-10'],
            'product_price': [100, 200, 150]
        })
        result = total_revenue_by_month(data)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
