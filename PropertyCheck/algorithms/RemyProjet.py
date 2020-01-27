import random
from collections import defaultdict
import pprint


class Node:

    def __init__(self, num):
        self.FG = -1
        self.FD = -1
        self.P = -1
        self.num = num

    def __str__(self):
        return "Num : " + str(self.num) + " P : " + str(self.P) + " FG : " + str(self.FG) + " FD : " + str(self.FD)

    def __repr__(self):
        return "Num : " + str(self.num) + " P : " + str(self.P) + " FG : " + str(self.FG) + " FD : " + str(self.FD)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.num == other.num and self.P == other.P and self.FG == other.FG and self.FD == other.FD


class ArbreRemy:
    arbre = None

    def __init__(self, N):
        self.arbre = [Node(i) for i in range(2 * N + 1)]

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
        return self

    def __eq__(self, other):
        if not isinstance(other, ArbreRemy):
            return False
        return self.arbre == other.arbre


def gen_perms(n: int, i: int) -> [[]]:
    if n < i:
        return [[]]
    elements = gen_perms(n, i + 1)
    res = []
    for i in range(i):
        for ele in elements:
            tmp = ele.copy()
            tmp.insert(0, i)
            res.append(tmp)
    return res


def gen_perm(n: int) -> [[]]:
    return gen_perms(n, 2)


def treeToStr(A: ArbreRemy, i: int = 0) -> str:
    if A.arbre[i].FG == -1 and A.arbre[i].FD == -1:
        return ""
    else:
        fg = A.arbre[i].FG
        fd = A.arbre[i].FD
        return "(" + treeToStr(A, fg) + ")" + treeToStr(A, fd)


def generate_all_trees_remy1(n: int) -> dict:
    dict = defaultdict(int)
    for i in gen_perm(n):
        tree = ArbreRemy(n)
        dict[treeToStr(tree.growingTreeComplete(n, i))] += 1
    return dict


pprint.pprint(generate_all_trees_remy1(2))
