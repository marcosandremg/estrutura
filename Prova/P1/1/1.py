from ods.arraydeque import ArrayDeque
from random import randrange as rd

test = ArrayDeque()
for _ in range(10):
    test.add(_, rd(0,20))

print(test)
test.remove_varios(3,6)
print(test)

