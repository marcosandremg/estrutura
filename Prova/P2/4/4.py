"""
Nome: Marcos André de Moraes Galdino
Matricula: 201810068311
Declaro que a resolução desta atividade, que submeto para avaliação, é meu trabalho individual,
realizado sem ajuda de qualquer outra pessoa, e constitui solução original criada por mim,
sem auxílio de terceiros ou cópia de trabalhos já publicados.

"""
from ods.binaryheap import BinaryHeap

a = BinaryHeap()
for _ in range(15):
    a.add(_)
print(a)
print(a.remove_two(1))
