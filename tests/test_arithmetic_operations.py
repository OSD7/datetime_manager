# tests/test_arithmetic_operations.py
import unittest
from datetime_manager import arithmetic_operations
from datetime import datetime

class TestArithmeticOperations(unittest.TestCase):
    def test_add_days(self):
        self.assertEqual(arithmetic_operations.add_days(datetime(2023, 1, 1), 1), datetime(2023, 1, 2))
    
    def test_subtract_days(self):
        self.assertEqual(arithmetic_operations.subtract_days(datetime(2023, 1, 1), 1), datetime(2022, 12, 31))

    def test_days_between(self):
        date1 = datetime(2023, 1, 1)
        date2 = datetime(2023, 1, 10)
        self.assertEqual(arithmetic_operations.days_between(date1, date2), 9)
    
    def test_seconds_between(self):
        date1 = datetime(2023, 1, 1, 0, 0, 0)
        date2 = datetime(2023, 1, 1, 1, 0, 0)
        self.assertEqual(arithmetic_operations.seconds_between(date1, date2), 3600)

if __name__ == '__main__':
    unittest.main()

