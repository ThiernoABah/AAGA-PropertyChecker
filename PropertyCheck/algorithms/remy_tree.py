import random
import math
import pprint

from remy_tree_v2 import *


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
        if self.arbre[parentA].FD == a:
            self.arbre[parentA].FD = b
        else:
            self.arbre[parentA].FG = b
        self.arbre[a].P = parentB
        if self.arbre[parentB].FD == b:
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

    def growingTreeComplete(self, n, liste):
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


def all_choice_remy1(n):
    res = list()
    tab = list()
    factN = math.factorial(n + 1)

    for i in range(n):
        tab.append(0)

    for i in range(factN):
        res.append(tab.copy())
        for j in range(n):
            if tab[j] < j + 1:
                tab[j] += 1
                break
            else:
                tab[j] = 0
    return res


def all_choice_remy2(n):
    res = list()
    tab = list()
    dico = dict()

    for i in range(n - 1):
        tab.append(0)

    while str(tab) not in dico:
        res.append(tab.copy())
        dico[str(tab)] = 1
        for j in range(n):
            if j < n - 1:
                if tab[j] < j + 2:
                    tab[j] += 1
                    break
                else:
                    tab[j] = 0
            else:
                tab[j - 1] += 2 * (n - 1)
    return res


def get_bin(x, n=0):
    return format(x, 'b').zfill(n)


def all_pileface(n):
    res = list()
    N = 2 ** (n - 1)
    for i in range(N):
        rpz = [int(char) for char in get_bin(i, (n - 1))]
        res.append(rpz)
    return res


def treeToStr(A: ArbreRemy, i=0):
    if A.arbre[i].FG == -1 and A.arbre[i].FD == -1:
        return "eps"
    else:
        fg = A.arbre[i].FG
        fd = A.arbre[i].FD
        return "(" + treeToStr(A, fg) + ")" + treeToStr(A, fd)


def create_all_tree_remy1(n):
    res = dict()

    for perm in all_choice_remy1(n):
        tree = ArbreRemy(n)

        tree.growingTreeComplete(n, perm)
        rpz = treeToStr(tree)
        if rpz in res:
            res[rpz] = res[rpz] + 1
        else:
            res[rpz] = 1
    return res


def create_all_tree_remy2(n):
    pileFaces = all_pileface(n)
    res_remy2 = dict()
    i = 0
    for perm in all_choice_remy2(n):
        for pf in pileFaces:
            tree_remy_v2 = remy_uniform_complete(n, perm, pf)
            rpz2 = print_tree(tree_remy_v2)
            if rpz2 in res_remy2:
                res_remy2[rpz2] = res_remy2[rpz2] + 1
            else:
                res_remy2[rpz2] = 1
            i += 1

    return res_remy2

size = 3
remyV1 = create_all_tree_remy1(size)
remyV2 = create_all_tree_remy2(size)
print()
print("here all tree of size ",size,"generate for all possible inputs using the first algorithm")
pprint.pprint(remyV1)
print()
print("here all tree of size ",size,"generate for all possible inputs using our algorithm")
pprint.pprint(remyV2)
