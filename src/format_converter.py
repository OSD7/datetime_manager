from datetime import datetime

def parse_date(date_string, yearfirst=True, monthfirst=False):
    if yearfirst:
        formats = ["%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d", "%Y%m%d"]
    elif monthfirst:
        formats = ["%m-%d-%Y", "%m.%d.%Y", "%m/%d/%Y", "%m%d%Y"]
    else:
        formats = [date_string]

    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            pass

    raise ValueError("Invalid date format")

def format_date(date_obj, yearfirst=True, monthfirst=False, format="%Y-%m-%d"):
    if yearfirst:
        return date_obj.strftime(format)
    elif monthfirst:
        return date_obj.strftime(format)
    else:
        return date_obj.strftime(format)
'''
# Example usage
date_str = "2008-01-01"
parsed_date = parse_date(date_str)
print(parsed_date)

date_obj = datetime(2008, 1, 1)
formatted_date = format_date(date_obj, format="%m-%d-%Y")
print(formatted_date)
'''