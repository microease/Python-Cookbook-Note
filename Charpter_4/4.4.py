# 你想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的
# 简单方法。
class Node:
    def __init__(self,value):
        self._value = value
