# 你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL
# Scheme 等等。
filename = 'spam.txt'
print(filename.endswith('.txt'))
res = filename.startswith('file:')
print(res)
url = 'http://www.baidu.com'
res = url.startswith('http:')
print(res)
import os
filenames = os.listdir('.')
print(filenames)
from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()