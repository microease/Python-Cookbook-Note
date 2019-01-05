# 你想在字符串中搜索和匹配指定的文本模式
text = 'yeah, but no, but yeah, but no, but yeah'
res = text.replace('yeah', 'yep')
print(res)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re

res = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(res)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


res = datepat.sub(change_date, text)
print(res)
