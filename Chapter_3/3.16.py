# 你有一个安排在 2012 年 12 月 21 日早上 9:30 的电话会议，地点在芝加哥。而你
# 的朋友在印度的班加罗尔，那么他应该在当地时间几点参加这个会议呢？
from datetime import datetime
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
bang_d = loc_d.astimezone(timezone('Asia/Shanghai'))
print(bang_d)
