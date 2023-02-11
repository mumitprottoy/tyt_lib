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


hours = tuple(['0'+str(x) for x in range(10)]+[str(y) for y in range(10,24)])
minutes = ('00', '30')


def get_readable_date(date_str):
    year, month_idx, day = date_str.split('-')
    return f"{months[int(month_idx)-1]} {day}, {year}"
