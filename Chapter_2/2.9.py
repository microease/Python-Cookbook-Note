# 你正在处理 Unicode 字符串，需要确保所有字符串在底层有相同的表示。
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
res = t1 == t2
print(res)
print(ascii(t1))
