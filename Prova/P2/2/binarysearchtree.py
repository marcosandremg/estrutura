"""An implementation of a binary search tree"""
from ods.binarytree import BinaryTree
from ods.base import BaseSet
"""
Nome: Marcos André de Moraes Galdino
Matricula: 201810068311
Declaro que a resolução desta atividade, que submeto para avaliação, é meu trabalho individual,
realizado sem ajuda de qualquer outra pessoa, e constitui solução original criada por mim,
sem auxílio de terceiros ou cópia de trabalhos já publicados.

"""

class BinarySearchTree(BinaryTree, BaseSet):
    """Base classs for all our binary search trees"""

    class Node(BinaryTree.Node):
        def __init__(self, x):
            super(BinarySearchTree.Node, self).__init__()
            self.x = x

    def _new_node(self, x):
        u = BinarySearchTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u

    def __init__(self, iterable=[], nil=None):
        super(BinarySearchTree, self).__init__()
        self._initialize()
        self.nil = nil
        self.add_all(iterable)

    def _initialize(self):
        self.n = 0

    def clear(self):
        self.r = self.nil
        self.n = 0

    def _find_last(self, x):
        w = self.r
        prev = self.nil
        while w is not self.nil:
            prev = w
            if (x < w.x):
                w = w.left
            elif (x > w.x):
                w = w.right
            else:
                return w
        return prev

    def _add_child(self, p, u):
        if p == self.nil:
            self.r = u  # inserting into empty tree
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False  # u.x is already in the tree
            u.parent = p
        self.n += 1
        return True

    def find_eq(self, x):
        w = self.r
        while w != self.nil:
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        return None

    def find(self, x):
        w = self.r
        z = self.nil
        while w != self.nil:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        if z == self.nil: return None
        return z.x

    def add(self, x):
        p = self._find_last(x)
        return self._add_child(p, self._new_node(x))

    def add_node(self, u):
        p = self._find_last(u.x)
        return self._add_child(p, u)

    def splice(self, u):
        if u.left != self.nil:
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            p = self.nil
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s != self.nil:
            s.parent = p
        self.n -= 1

    def _remove_node(self, u):
        if u.left == self.nil or u.right == self.nil:
            self.splice(u)
        else:
            w = u.right
            while w.left != self.nil:
                w = w.left
            u.x = w.x
            self.splice(w)

    def remove(self, x):
        u = self._find_last(x)
        if u != self.nil and x == u.x:
            self._remove_node(u)
            return True
        return False

    def rotate_left(self, u):
        w = u.right
        w.parent = u.parent
        if w.parent != self.nil:
            if w.parent.left == u:
                w.parent.left = w
            else:
                w.parent.right = w
        u.right = w.left
        if u.right != self.nil:
            u.right.parent = u
        u.parent = w
        w.left = u
        if u == self.r:
            self.r = w
            self.r.parent = self.nil

    def rotate_right(self, u):
        w = u.left
        w.parent = u.parent
        if w.parent != self.nil:
            if w.parent.left == u:
                w.parent.left = w
            else:
                w.parent.right = w
        u.left = w.right
        if u.left != self.nil:
            u.left.parent = u
        u.parent = w
        w.right = u
        if u == self.r:
            self.r = w
            self.r.parent = self.nil

    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)

    def count_left(self, u=0):
        if u == 0:
            u = self.r
        i = 0
        if u.left and u.right is not self.nil:
            i = i + self.count_left(u.left)
            i = i + self.count_left(u.right)
        elif u.right is not self.nil:
            i = i + self.count_left(u.right)
        elif u.left is not self.nil:
            i = i + self.count_left(u.left)
        if u.parent is not self.nil and u.parent.left == u:
            if u.right or u.left is not self.nil:
                return i
            else:
                i += 1
                return i
        return i
