# 你想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白。
s = 'hello world \n'
print(s)
res = s.strip()
print(res)
res = s.rstrip()
print(res)
res = s.lstrip()
print(res)
