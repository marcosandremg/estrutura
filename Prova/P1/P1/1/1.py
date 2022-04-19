from ods.arraydeque import ArrayDeque
from random import randrange as rd

test = ArrayDeque()
for _ in range(0, 20):
    test.add(_, rd(0,20))

print(test)
test.remove_varios(2,9)
print(test)

