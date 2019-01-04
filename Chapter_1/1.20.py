# 现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某
# 些操作，比如查找值或者检查某些键是否存在。
a = {
    'x': 1,
    'z': 3,
}
b = {
    'y': 2,
    'z': 4,
}
from collections import ChainMap

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])
print(len(c))
print(list(c.keys()))
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)