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
