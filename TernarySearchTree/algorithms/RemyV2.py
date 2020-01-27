import math
from collections import defaultdict
from random import *


class Rand48(object):
    def __init__(self, seed):
        if seed < 2 ** 40:
            seed += 2 ** 40
        self.n = seed

    def seed(self, seed):
        self.n = seed

    def srand(self, seed):
        self.n = (seed << 16) + 0x330e

    def next(self):
        self.n = (25214903917 * self.n + 11) & (2 ** 48 - 1)
        return self.n

    def drand(self):
        return self.next() / 2 ** 48

    def lrand(self):
        return self.next() >> 17

    def mrand(self):
        n = self.next() >> 16
        if n & (1 << 31):
            n -= 1 << 32
        return n


class Rand48_(Rand48):
    def __init__(self, seed):
        super(Rand48_, self).__init__(seed)
        self.entier = None
        self.bit_count = 0

    def bit_suivant(self):
        if self.bit_count > 0:
            res = self.entier & 1
            self.entier = self.entier >> 1
            self.bit_count -= 1
            return res
        else:
            self.entier = super(Rand48_, self).mrand()
            self.bit_count += 48
            return self.bit_suivant()

    def gen_n(self, n):
        nb_bits = int(math.ceil(math.log(n, 2)))
        res = 0
        for i in range(nb_bits):
            res = (res << 1) | self.bit_suivant()

        if res > n:
            return self.gen_n(n)
        return res


class BinaryTree(object):
    def __init__(self, left=False, right=False, father=None):
        self.left = left
        self.right = right
        self.father = father

    def set_father(self, f):
        self.father = f

    def is_feuille(self):
        return not self.left and not self.right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def __repr__(self):
        if self.is_feuille():
            return "eps"
        return "( " + str(self.left) + " " + str(self.right) + " )"


rand48_ = Rand48_(randint(2 ** 40, 2 ** 48))


def RemyV2(n):
    if n == 0:
        return BinaryTree(father=False)

    k = 1

    left = BinaryTree(father=False)
    right = BinaryTree(father=False)
    root = BinaryTree(father=False, left=left, right=right)

    left.set_father(root)
    right.set_father(root)

    idNodTree = [root, left, right]

    while k < n:
        id_rand = randint(0, len(idNodTree) - 1)
        F = idNodTree[id_rand]

        E = BinaryTree(father=F.father)
        if F.father:
            if F == F.father.right:
                F.father.set_right(E)
            elif F == F.father.left:
                F.father.set_left(E)
        F.set_father(E)

        leaf = BinaryTree(father=E)

        if k % 2 == 0:
            E.set_left(F)
            E.set_right(leaf)
        else:
            E.set_right(F)
            E.set_left(leaf)

        idNodTree.append(E)
        idNodTree.append(leaf)
        k = k + 1
    node = idNodTree[0]
    while node.father:
        node = node.father

    return node


def print_tree(A):
    if A.left == False and A.right == False:
        return "eps"
    return "(" + print_tree(A.left) + ")" + print_tree(A.right)
