"""
Nome: Marcos André de Moraes Galdino
Matricula: 201810068311
Declaro que a resolução desta atividade, que submeto para avaliação, é meu trabalho individual,
realizado sem ajuda de qualquer outra pessoa, e constitui solução original criada por mim,
sem auxílio de terceiros ou cópia de trabalhos já publicados.

"""
from ods.binarysearchtree import BinarySearchTree

a = BinarySearchTree()
a.add(50)
a.add(71)
a.add(38)
a.add(80)
a.add(75)
a.add(59)
a.add(55)
a.add(40)
a.add(39)
a.add(27)

print(a.count_left())
