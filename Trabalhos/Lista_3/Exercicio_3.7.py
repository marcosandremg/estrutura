from ods.dllist import DLList
import random

a = DLList()
for j in range(5):
    a.add(a.size(), j)
for j in range(5, -1, -1):
    a.add(a.size(), j)

print(a.eh_palindromo())
