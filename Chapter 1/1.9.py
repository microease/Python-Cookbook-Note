<<<<<<< HEAD
=======
# coding=utf-8
>>>>>>> 884c6a401d29257f4ce2f4c957671f2a2042d5b6
# 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？
a = {
    'x': 1,
    'y': 2,
<<<<<<< HEAD
    'z': 3,
=======
    'z': 3
>>>>>>> 884c6a401d29257f4ce2f4c957671f2a2042d5b6
}

b = {
    'w': 10,
    'x': 11,
    'y': 2,
}
<<<<<<< HEAD
# 找到2个字典中相同的key
print(a.keys() & b.keys())
# 找到在a字典中不在b字典中的key
print(a.keys() - b.keys())
# 找到2个字典中key和value都相同的元素
print(a.items() & b.items())
# 修改或过滤字典元素
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)
=======
# 找到都有的key
print(a.keys() & b.keys())
# 找到a里面有的b里面没有的
print(a.keys() - b.keys())
# 找到key和value都相同的元素：
print(a.items() & b.items())
>>>>>>> 884c6a401d29257f4ce2f4c957671f2a2042d5b6
