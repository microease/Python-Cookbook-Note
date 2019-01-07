# 你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
multiline comment */ .
'''
res = comment.findall(text1)
print(res)
res = comment.findall(text2)
print(res)
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
res = comment.findall(text2)
print(res)
