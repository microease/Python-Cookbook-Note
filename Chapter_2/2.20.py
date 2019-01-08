# 你想在字节字符串上执行普通的文本操作 (比如移除，搜索和替换)。
data = b'hello world'
print(data[0:5])
print(data.startswith(b'hello'))
print(data.replace(b'hello', b'hello cruel'))
data = bytearray(b'hello world')
print(data[0:5])
s = b'hello world'
print(s)
print(s.decode('ascii'))
res = '{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
print(res)
