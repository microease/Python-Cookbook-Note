# 怎样找出一个序列中出现次数最多的元素呢？
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not',
         'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're",
         'under']
from collections import Counter
words_counts = Counter(words)
# 出现频率最高的三个单词：
top_three = words_counts.most_common(3)
print(top_three)
