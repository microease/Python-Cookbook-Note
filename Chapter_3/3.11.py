# 你想从一个序列中随机抽取若干元素，或者想生成几个随机数。
import random
values = [1, 2, 3, 4, 5, 6]
res = random.choice(values)
print(res)
res = random.sample(values,3)
print(res)
res = random.shuffle(values)
print(res)
res = random.random()
print(res)
