# 你正在使用正则表达式处理文本，但是关注的是 Unicode 字符处理。
import re
num = re.compile('\d+')
res = num.match('123')
print(res)
pat = re.compile('stra\u00dfe', re.IGNORECASE)