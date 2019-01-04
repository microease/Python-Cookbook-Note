# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？
price = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(price.values(),price.keys()))
test = zip(price.values(),price.keys())
print(test)
print(min_price)
max_price = max(zip(price.values(),price.keys()))
print(max_price)
price_sorted = sorted(zip(price.values(),price.keys()))