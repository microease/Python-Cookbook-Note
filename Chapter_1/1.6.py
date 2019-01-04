# 怎样实现一个键对应多个值的字典（也叫 multidict）？
from collections import defaultdict

d = {
    'a': [1, 2, 3],
    'b': [4, 5],
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5},
}

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
print(d)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(3)
print(d)
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
print(d)
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
        d[key].append(value)

