from ods.dllist import DLList
import random

a = DLList()
for j in range(10):
    a.add(a.size(), random.randrange(0, 16))

print(a)
a.rotate(13)
print(a)