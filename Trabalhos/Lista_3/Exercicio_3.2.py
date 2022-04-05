from ods.sllist import SLList
import random

a = SLList()
for j in range(10):
    a.add(a.size(), random.randrange(0, 100))

print(a)
print(a.penultimate())
