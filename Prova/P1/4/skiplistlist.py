"""A skiplist implementation of the List interface

W. Pugh. Skip Lists: A probabilistic alternative to balanced trees. 
  In Communications of the ACM, 33(6), pp. 668-676, June 1990.

W. Pugh. A skip list cookbook. CS-TR-2286.1, University of Maryland, 
  College Park, 1990.
"""
import random
import numpy
from ods.utils import new_array
from ods.base import BaseList


class SkiplistList(BaseList):
    class Node(object):
        """A node in a skip list"""

        def __init__(self, x, h):
            self.x = x
            self.next = new_array(h + 1)
            self.length = numpy.ones(h + 1, dtype=int)

        def height(self):
            return len(self.next) - 1

    def _new_node(self, x, h):
        return SkiplistList.Node(x, h)

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.h = 0
        self.n = 0
        self.sentinel = self._new_node(None, 32)
        self.stack = new_array(self.sentinel.height() + 1)

    def find_pred(self, i):
        u = self.sentinel
        r = self.h
        j = -1
        while r >= 0:
            while u.next[r] is not None and j + u.length[r] < i:
                j += u.length[r]
                u = u.next[r]  # go right in list r
            r -= 1  # go down into list r-1
        return u

    def get(self, i):
        if i < 0 or i > self.n - 1: raise IndexError()
        return self.find_pred(i).next[0].x

    def set(self, i, x):
        if i < 0 or i > self.n - 1: raise IndexError()
        u = self.find_pred(i).next[0]
        y = u.x
        u.x = x
        return y

    def _add(self, i, w):
        u = self.sentinel
        k = w.height()
        r = self.h
        j = -1
        while r >= 0:
            while u.next[r] is not None and j + u.length[r] < i:
                j += u.length[r]
                u = u.next[r]
            u.length[r] += 1
            if r <= k:
                w.next[r] = u.next[r]
                u.next[r] = w
                w.length[r] = u.length[r] - (i - j)
                u.length[r] = i - j
            r -= 1
        self.n += 1
        return u

    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        w = self._new_node(x, self.pick_height())
        if w.height() > self.h:
            self.h = w.height()
        self._add(i, w)

    def remove(self, i):
        if i < 0 or i > self.n - 1: raise IndexError()
        u = self.sentinel
        r = self.h
        j = -1
        while r >= 0:
            while u.next[r] is not None and j + u.length[r] < i:
                j += u.length[r]
                u = u.next[r]
            u.length[r] -= 1
            if j + u.length[r] + 1 == i and u.next[r] is not None:
                x = u.next[r].x
                u.length[r] += u.next[r].length[r]
                u.next[r] = u.next[r].next[r]
                if u == self.sentinel and u.next[r] is None:
                    self.h -= 1
            r -= 1
        self.n -= 1
        return x

    def __iter__(self):
        u = self.sentinel.next[0]
        while u is not None:
            yield u.x
            u = u.next[0]

    def pick_height(self):
        z = random.getrandbits(32)
        k = 0
        while z & 1:
            k += 1
            z = z // 2
        return k

    def trasnsfer(self, i):
        if i < 0 or i > self.n - 1: raise IndexError()
        l2 = SkiplistList()
        for j in range(random.randrange(0, 15)):  # Montando l2 de forma aleatória
            l2.add(j, random.randrange(0, 20))
        if (l2.n - 1) >= i: raise IndexError()

        u = l2.sentinel
        r = l2.h
        j = -1
        cont = 0
        while r >= 0:
            while u.next[r] is not None and j + u.length[r] < i:
                if j + u.length[r] - 1 == i:
                    cont += 1
                j += u.length[r]
                u = u.next[r]
            r -= 1
        a = u.next[0].x
        self._add_2(i, a, cont)
        l2.remove(i)

    def _add_2(self, i, x, cont):
        if i < 0 or i > self.n: raise IndexError()
        w = self._new_node(x, cont)
        if w.height() > self.h:
            self.h = w.height()
        self._add(i, w)
