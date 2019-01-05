# 你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹 配。而你想修改它变成查找最短的可能匹配。
import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
res = str_pat.findall(text1)
print(res)
text2 = 'Computer says "no." Phone says "yes."'
res = str_pat.findall(text2)
print(res)
str_pat = re.compile(r'\"(.*?)\"')
res = str_pat.findall(text2)
print(res)
