# 你想将几个小的字符串合并为一个大的字符串
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
res = ' '.join(parts)
print(res)
a = 'Is Chicago'
b = 'Not Chicage?'
res = a + ' ' + b
print(res)
data = ['ACME', 50, 91.1]
res = ','.join(str(d) for d in data)
print(res)
