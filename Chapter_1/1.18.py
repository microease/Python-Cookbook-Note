# 你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的
# 代码难以阅读，于是你想通过名称来访问元素。
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


s = Stock('ACME', 100, 123.45)
print(s)
print(s.price)
s = s._replace(price=111)
print(s.price)

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
