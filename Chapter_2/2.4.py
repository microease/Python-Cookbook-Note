# 你想匹配或者搜索特定模式的文本
text = 'yeah, but no, but yeah, but no, but yeah'

res = text == 'yeah'
print(res)

res = text.startswith('yeah')
print(res)

res = text.endswith('no')
print(res)

res = text.find('no')
print(res)

text1 = '11/27/2012'
text2 = 'Nov 27.2012'
import re

if re.match(r'\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+', text2):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'\d+/\d+/\d+')
res = datepat.findall(text)
print(res)
