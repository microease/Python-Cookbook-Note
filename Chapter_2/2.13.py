# 你想通过某种对齐方式来格式化字符串
text = 'Hello World'
res = text.ljust(20)
print(res)
res = text.rjust(20)
print(res)
res = text.center(20)
print(res)
res = text.rjust(20,'=')
print(res)
res = format(text,'>20')
print(res)