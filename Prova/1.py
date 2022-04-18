from ods.arraydeque import ArrayDeque
from random import randrange as rd

teste = ArrayDeque()
for _ in range(0,10):
    teste.add(_, rd(1, 100))

print(teste)
