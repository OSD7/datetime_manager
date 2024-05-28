# tests/test_timezone_manager.py
import unittest
from datetime_manager import timezone_manager
from datetime import datetime
import pytz

class TestTimezoneManager(unittest.TestCase):
    def test_convert_timezone(self):
        date_obj = datetime(2023, 1, 1, 12, 0, 0)
        from_tz = "UTC"
        to_tz = "US/Pacific"
        converted = timezone_manager.convert_timezone(date_obj, from_tz, to_tz)
        self.assertEqual(converted.strftime("%Y-%m-%d %H:%M:%S %Z%z"), "2023-01-01 04:00:00 PST-0800")
    
    def test_get_current_time_in_timezone(self):
        tz_name = "Asia/Seoul"
        current_time = timezone_manager.get_current_time_in_timezone(tz_name)
        self.assertTrue(current_time.tzinfo is not None)
        self.assertEqual(current_time.tzinfo.zone, tz_name)

if __name__ == '__main__':
    unittest.main()
   
