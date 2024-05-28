 # tests/test_format_converter.py
import unittest
from datetime_manager import format_converter
from datetime import datetime

class TestFormatConverter(unittest.TestCase):
    def test_str_to_datetime(self):
        self.assertEqual(format_converter.str_to_datetime("2023-01-01 00:00:00"), datetime(2023, 1, 1, 0, 0, 0))
    
    def test_datetime_to_str(self):
        self.assertEqual(format_converter.datetime_to_str(datetime(2023, 1, 1, 0, 0, 0)), "2023-01-01 00:00:00")
    
    def test_reformat_datetime(self):
        self.assertEqual(format_converter.reformat_datetime("2023-01-01 00:00:00", "%Y-%m-%d %H:%M:%S", "%d-%m-%Y %I:%M %p"), "01-01-2023 12:00 AM")

if __name__ == '__main__':
    unittest.main()

