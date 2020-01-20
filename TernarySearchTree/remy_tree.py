import random
import math


class Remy:
    FG = -12
    FD = -13
    P = -14
    num = -1

    def __init__(self, FG, FD, P, num):
        self.FG = FG
        self.FD = FD
        self.P = P
        self.num = num

    def __str__(self):
        return "Num : " + str(self.num) + " P : " + str(self.P) + " FG : " + str(self.FG) + " FD : " + str(self.FD)

    def __repr__(self):
        return "Num : " + str(self.num) + " P : " + str(self.P) + " FG : " + str(self.FG) + " FD : " + str(self.FD)

    def __eq__(self, other):
        if not isinstance(other, Remy):
            return False
        return self.num == other.num and self.P == other.P and self.FG == other.FG and self.FD == other.FD


class ArbreRemy:
    arbre = None

    def __init__(self, N):
        self.arbre = [Remy(-1, -1, -1, i) for i in range(2 * N + 1)]

    def changeLeaves(self, a, b):
        parentA = self.arbre[a].P
        parentB = self.arbre[b].P
        if (self.arbre[parentA].FD == a):
            self.arbre[parentA].FD = b
        else:
            self.arbre[parentA].FG = b
        self.arbre[a].P = parentB
        if (self.arbre[parentB].FD == b):
            self.arbre[parentB].FD = a
        else:
            self.arbre[parentB].FG = a
        self.arbre[b].P = parentA

    def growingTree(self, n):
        if n == 0:
            return
        elif n == 1:
            self.arbre[0].num = 1
            return

        self.arbre[0].FG = 1
        self.arbre[0].FD = 2
        self.arbre[0].num = 0
        self.arbre[1].P = self.arbre[2].P = 0
        self.arbre[1].FD = self.arbre[1].FG = -1
        self.arbre[2].FD = self.arbre[2].FG = -1

        for i in range(2, n + 1):
            nb = random.randint(0, i - 1)
            self.changeLeaves(i - 1, nb + i - 1)
            self.arbre[i - 1].FD = 2 * i - 1
            self.arbre[i - 1].FG = 2 * i
            self.arbre[i - 1].num = i - 1
            self.arbre[2 * i - 1].P = self.arbre[2 * i].P = i - 1
            self.arbre[2 * i - 1].FD = self.arbre[2 * i - 1].FG = -1
            self.arbre[2 * i].FD = self.arbre[2 * i].FG = -1

    def growingTree2(self, n, liste):
        if n == 0:
            return
        elif n == 1:
            self.arbre[0].num = 1
            return

        self.arbre[0].FG = 1
        self.arbre[0].FD = 2
        self.arbre[0].num = 0
        self.arbre[1].P = self.arbre[2].P = 0
        self.arbre[1].FD = self.arbre[1].FG = -1
        self.arbre[2].FD = self.arbre[2].FG = -1

        for i, nb in zip(range(2, n + 1), liste):
            # nb = liste(i-2)
            self.changeLeaves(i - 1, nb + i - 1)
            self.arbre[i - 1].FD = 2 * i - 1
            self.arbre[i - 1].FG = 2 * i
            self.arbre[i - 1].num = i - 1
            self.arbre[2 * i - 1].P = self.arbre[2 * i].P = i - 1
            self.arbre[2 * i - 1].FD = self.arbre[2 * i - 1].FG = -1
            self.arbre[2 * i].FD = self.arbre[2 * i].FG = -1

    def __eq__(self, other):
        if not isinstance(other, ArbreRemy):
            return False
        return self.arbre == other.arbre


def permutation(liste):
    if len(liste) == 0:
        return [[]]
    else:
        return [[x] + ys for x in liste for ys in permutation(delete(liste, x))]


def delete(liste, item):
    lc = liste[:]
    lc.remove(item)
    return lc


def all_val(n):
    res = list()
    factN = math.factorial(n + 1)
    for j in range(factN):
        res.append([0 for i in range(n)])

    for k in range(n):
        cpt = 0
        for j in range(factN):
            res[j][k] = cpt
            cpt += 1
            if cpt != 0 and (cpt % (k + 2)) == 0:
                cpt = 0
    return res


def treeToStr(A: ArbreRemy, i=0):
    if A.arbre[i].FG == -1 and A.arbre[i].FD == -1:
        return "eps"
    else:
        fg = A.arbre[i].FG
        fd = A.arbre[i].FD
        return "(" + treeToStr(A, fg) + ")" + treeToStr(A, fd)


def create_all_tree(n):
    res = dict()

    for perm in all_val(n):
        tree = ArbreRemy(n)
        tree.growingTree2(n, perm)
        rpz = treeToStr(tree)
        if (rpz in res):
            res[rpz] = res[rpz] + 1
        else:
            res[rpz] = 1
    return res


remy = ArbreRemy(0)
remy1 = ArbreRemy(10)
remy2 = ArbreRemy(10)

remy.growingTree(0)
remy1.growingTree2(10, [0, 2, 1, 4, 3, 5, 0, 1, 7])
remy2.growingTree2(10, [0, 2, 1, 4, 3, 5, 0, 1, 7])

import pprint

# print(remy1 == remy2)
# pprint.pprint(remy2.arbre)

# remy2 = ArbreRemy(2)
# remy2.growingTree2(2, [0, 1])
# print()
# pprint.pprint(remy2.arbre)
pprint.pprint(create_all_tree(3))
