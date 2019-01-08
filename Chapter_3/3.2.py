# 你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现。
a = 4.2
b = 2.1
print(a + b)
from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)

from decimal import localcontext

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)
