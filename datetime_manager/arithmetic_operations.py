# datetime_manager/arithmetic_operations.py
from datetime import datetime, timedelta

def add_days(date_obj, days):
    return date_obj + timedelta(days=days)

def subtract_days(date_obj, days):
    return date_obj - timedelta(days=days)

def days_between(date1, date2):
    delta = date2 - date1
    return delta.days

def seconds_between(date1, date2):
    delta = date2 - date1
    return delta.total_seconds()
  
