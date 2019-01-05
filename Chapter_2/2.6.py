# 你需要以忽略大小写的方式搜索与替换文本字符串

import re
text = 'UPPER PYTHON, lower python, Mixed Python'
res = re.findall('python',text,flags=re.IGNORECASE)
print(res)

res = re.sub('python','snake',text,flags=re.IGNORECASE)
print(res)