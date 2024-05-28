from datetime import datetime
import pytz

def parse_date_with_timezone(date_string, timezone, yearfirst=True, monthfirst=False):
    if yearfirst:
        formats = ["%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d", "%Y%m%d"]
    elif monthfirst:
        formats = ["%m-%d-%Y", "%m.%d.%Y", "%m/%d/%Y", "%m%d%Y"]
    else:
        formats = [date_string]

    for fmt in formats:
        try:
            parsed_date = datetime.strptime(date_string, fmt)
            return timezone.localize(parsed_date)
        except ValueError:
            pass

    raise ValueError("Invalid date format")

def format_date_with_timezone(date_obj, timezone, format="%Y-%m-%d"):
    return date_obj.astimezone(timezone).strftime(format)

''' Example usage
date_str = "2008-01-01"
timezone = pytz.timezone('America/New_York')

parsed_date = parse_date_with_timezone(date_str, timezone)
print(parsed_date)

date_obj = datetime(2008, 1, 1)
formatted_date = format_date_with_timezone(date_obj, timezone, format="%m-%d-%Y")
print(formatted_date)
'''