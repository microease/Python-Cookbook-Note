# 解压可迭代对象赋值给多个变量
# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

def drop_first_last(grades):
    first, *middle, last = grades
    print(middle)


grades = 1, 2, 3, 4, 5
drop_first_last(grades)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name, email, phone_numbers)

sales_record = [10, 8, 7, 1, 9, 5, 10, 3]


def test1():
    *trailing_qtrs, current_qtr = sales_record
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    print(trailing_qtrs, current_qtr)
    print(trailing_avg)
    # return avg_comparison(trailing_avg, current_qtr)


test1()

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, fields, homedir, sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))
