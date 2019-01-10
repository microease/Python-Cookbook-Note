# 你的代码需要在当前月份中循环每一天，想找到一个计算这个日期范围的高效方
# 法。
from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, day_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_day = start_date + timedelta(days=day_in_month)
    return (start_date, end_day)


a_day = timedelta(days=1)
first_day, last_day = get_month_range()
print(first_day, last_day)
