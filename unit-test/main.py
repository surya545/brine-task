import unittest
from components.test_total_revenue_by_customer import TestTotalRevenueByCustomer
from components.test_total_revenue_by_month import TestTotalRevenueByMonth
from components.test_total_revenue_by_product import TestTotalRevenueByProduct
from components.test_top_10_customers import TestTop10Customers
from components.test_read_data import TestReadData

if __name__ == '__main__':
    # Create a test suite combining all test classes
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTotalRevenueByCustomer))
    test_suite.addTest(unittest.makeSuite(TestTotalRevenueByMonth))
    test_suite.addTest(unittest.makeSuite(TestTotalRevenueByProduct))
    test_suite.addTest(unittest.makeSuite(TestReadData))
    test_suite.addTest(unittest.makeSuite(TestTop10Customers))

    # Run the test suite
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
