# 你想遍历一个可迭代对象中的所有元素，但是却不想使用 for 循环。

def manual_iter():
    with open('etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line,end='')
        except StopIteration:
            pass

items = [1,2,3,4,5,6,7,8,9,10]
it = iter(items)
for i in range(10):
    print(next(it))