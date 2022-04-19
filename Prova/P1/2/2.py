from ods.sllist import SLList
from random import randrange

lista = SLList()
for j in range(20):
    lista.add(lista.size(), randrange(0, 20))

print(lista)
lista.particiona(11)
print(lista)