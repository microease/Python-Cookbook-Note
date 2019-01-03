# 怎样在一个序列上面保持元素顺序的同时消除重复的值？
# 解决：如果是不可变类型：使用集合或者生成器
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
res = list(dedupe(a))
print(res)


def dedupe1(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
res = list(dedupe1(a,key=lambda d:(d['x'],d['y'])))
print(res)

