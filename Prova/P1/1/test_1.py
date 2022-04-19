'''
Declaro que a resolução desta atividade, que submeto para avaliação,é meu trabalho individual, realizado sem ajuda
de qualquer outra pessoa, e constitui solução original criada por mim, sem auxílio de terceiros ou cópia de trabalhos
já publicados.

'''
from ods.arraydeque import ArrayDeque
from random import randrange as rd

test = ArrayDeque()
for _ in range(10):
    test.add(_, rd(0,20))

print(test)
test.remove_varios(3,6)
print(test)

