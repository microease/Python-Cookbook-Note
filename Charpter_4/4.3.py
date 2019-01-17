# 你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不
# 一样。
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 4, 0.5)))
