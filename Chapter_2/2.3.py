from fnmatch import fnmatch, fnmatchcase

res = fnmatch('foo.txt', '*.txt')
print(res)
res = fnmatch('Dat45.csv', 'Dat[0-9]*')
print(res)
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
