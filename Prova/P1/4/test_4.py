'''
Declaro que a resolução desta atividade, que submeto para avaliação,é meu trabalho individual, realizado sem ajuda
de qualquer outra pessoa, e constitui solução original criada por mim, sem auxílio de terceiros ou cópia de trabalhos
já publicados.

'''
from ods.skiplistlist import SkiplistList
import random


list = SkiplistList()
for j in range(10):
    list.add(j, random.randrange(0, 20))

list.trasnsfer(9)
