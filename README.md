# datetime_manager

A package for managing dates and times in Python.

## Installation

```bash
pip install datetime_manager

from datetime_manager import format_converter, arithmetic_operations, timezone_manager

# Convert string to datetime
dt = format_converter.str_to_datetime("2023-01-01 00:00:00")

# Format datetime to string
date_str = format_converter.datetime_to_str(dt)

# Reformat datetime string
reformatted = format_converter.reformat_datetime("2023-01-01 00:00:00", "%Y-%m-%d %H:%M:%S", "%d-%m-%Y %I:%M %p")

# Add days to a date
new_date = arithmetic_operations.add_days(dt, 5)

# Subtract days from a date
new_date = arithmetic_operations.subtract_days(dt, 5)

# Calculate days between two dates
days = arithmetic_operations.days_between(date1, date2)

# Calculate seconds between two dates
seconds = arithmetic_operations.seconds_between(date1, date2)

# Convert timezone
converted_date = timezone_manager.convert_timezone(dt, "UTC", "US/Pacific")

# Get current time in specific timezone
current_time = timezone_manager.get_current_time_in_timezone("Asia/Seoul")
