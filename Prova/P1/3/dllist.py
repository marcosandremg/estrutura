"""A doubly-linked list implementation with O(1+min{i, n-i}) update time"""
from ods.base import BaseList

class DLList(BaseList):
    
    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.n = 0
        self.dummy = DLList.Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get_node(self, i):
        if i < self.n/2:
            p = self.dummy.next    
            for _ in range(i): 
                p = p.next
        else:
            p = self.dummy
            for _ in range(self.n, i, -1): 
                p = p.prev
        return p

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        x = self.get_node(i).x
        self.move_para_frente(i)
        return x

    def set(self, i, x): #@ReservedAssignment
        if i < 0 or i >= self.n: raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def _remove(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1    

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        self._remove(self.get_node(i))

    def add_before(self, w, x):
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        self.add_before(self.get_node(i), x)

    def __iter__(self):
        u = self.dummy.next
        while u != self.dummy:
            yield u.x
            u = u.next

    def eh_palindromo(self):
        i = 0
        lenght = self.size() - 1
        a = True
        while i < (self.size() / 2):
            a = self.get(i)
            b = self.get(lenght - i)
            if a != b:
                i = self.size()
                a = False
            i += 1
        if a: return "É Palindromo"
        else: return "Não É Palindromo"

    def rotate(self, r):
        mod = self.size()
        j = r % mod
        a = self.get(j)
        self.set(j, self.get(0))
        i = 1
        while i < self.size():
            b = a
            j = (j + r) % mod
            a = self.get(j)
            self.set(j, b)
            i += 1

    def move_para_frente(self, i):
        u = self.get_node(i)
        t = u.prev
        b = u.next
        w = self.dummy.next
        s = w.next
        self.dummy.next = u
        u.prev = self.dummy
        u.next = s
        s.prev = u
        w.next = b
        w.prev = t
        t.next = w
        b.prev = w
