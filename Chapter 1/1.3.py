# 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
# 保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码
# 在多行上面做简单的文本匹配，并返回匹配所在行的最后 N 行：
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# if __name__ == '__main__':
#     with open(r'../Chapter 1/somefile.txt') as f:
#         for line, prevlines in search(f, 'python', 5):
#             print("line:" + line)
#             print("prevlines:" + str(prevlines))
#             print("**********")
#             for pline in prevlines:
#                 print(line, end='')
#                 print(pline, end='')
#                 print('-' * 20)

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.appendleft(0)
q.pop()
print(q)
