weekdays = (
    'Mon', 
    'Tue', 
    'Wed', 
    'Thu', 
    'Fri', 
    'Sat', 
    'Sun'
    )
months = (
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec',
    )

def get_readable_date(date_str):
    year, month_idx, day = date_str.split('-')
    return f"{months[int(month_idx)-1]} {day}, {year}"
