s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
res = html.escape(s)
print(res)

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = html.unescape(s)

print(p)
