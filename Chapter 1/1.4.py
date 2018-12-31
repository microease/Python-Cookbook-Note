# 怎样从一个集合中获得最大或者最小的 N 个元素列表？
# heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # 输出值：[42, 37, 23]
print(heapq.nsmallest(3, nums))  # 输出：[-4, 1, 2]
# 两个函数都能接受一个关键字参数，用于更复杂的数据结构中：
protfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, protfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, protfolio, key=lambda s: ['price'])
# print(cheap)
# print(expensive)
print("*" * 30)
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heapq.heappop(heap))