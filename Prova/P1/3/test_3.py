'''
Declaro que a resolução desta atividade, que submeto para avaliação,é meu trabalho individual, realizado sem ajuda
de qualquer outra pessoa, e constitui solução original criada por mim, sem auxílio de terceiros ou cópia de trabalhos
já publicados.

'''
from ods.dllist import DLList
from random import randrange

lista = DLList()
for j in range(10):
    lista.add(lista.size(), randrange(0, 20))

for _ in range(4):
    print(lista)
    y = randrange(0, 10)
    print(y)
    print(lista.get(y))

print(lista)
