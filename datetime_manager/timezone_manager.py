# datetime_manager/timezone_manager.py
from datetime import datetime
import pytz

def convert_timezone(date_obj, from_tz, to_tz):
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    date_obj = from_zone.localize(date_obj)
    return date_obj.astimezone(to_zone)

def get_current_time_in_timezone(tz_name):
    tz = pytz.timezone(tz_name)
    return datetime.now(tz)
  
