'''
Declaro que a resolução desta atividade, que submeto para avaliação,é meu trabalho individual, realizado sem ajuda
de qualquer outra pessoa, e constitui solução original criada por mim, sem auxílio de terceiros ou cópia de trabalhos
já publicados.

'''
from ods.sllist import SLList
from random import randrange

lista = SLList()
for j in range(20):
    lista.add(lista.size(), randrange(0, 20))

print(lista)
lista.particiona(11)
print(lista)