line = 'asdf fjdk; afed, fjek,asdf, foo'
import re

res = re.split(r'[;,\s]\s*', line)
print(res)

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
print(values)
delimiters = fields[1:2]+['']
print(delimiters)