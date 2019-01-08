# 你想在字节字符串上执行普通的文本操作 (比如移除，搜索和替换)。
data = b'hello world'
print(data[0:5])
print(data.startswith(b'hello'))
print(data.replace(b'hello',b'hello cruel'))
data = bytearray(b'hello world')
print(data[0:5])