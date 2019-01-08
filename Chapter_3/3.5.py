# 字节到大整数的打包与解包

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

res = len(data)
print(res)

res = int.from_bytes(data, 'little')
print(res)
res = int.from_bytes(data, 'big')
print(res)

x = 94522842520747284487117727783387188
res = x.to_bytes(16, 'big')
print(res)
import struct
