from ods.skiplistlist import SkiplistList
import random


list = SkiplistList()
for j in range(10):
    list.add(j, random.randrange(0, 20))

list.trasnsfer(9)
