# datetime_manager/format_converter.py
from datetime import datetime

def str_to_datetime(date_str, fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(date_str, fmt)

def datetime_to_str(date_obj, fmt="%Y-%m-%d %H:%M:%S"):
    return date_obj.strftime(fmt)

def reformat_datetime(date_str, from_fmt="%Y-%m-%d %H:%M:%S", to_fmt="%d-%m-%Y %I:%M %p"):
    date_obj = str_to_datetime(date_str, from_fmt)
    return datetime_to_str(date_obj, to_fmt)
  
