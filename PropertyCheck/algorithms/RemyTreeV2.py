from random import *
from collections import defaultdict

import math
from collections import defaultdict
from random import *

"""
Fichier contenant 
    notre version l'algorithime de Remy et 
    la méthode qui permet de générer les toutes les permutations possible 
        pour les arbre de taille n 
    la méthode qui permet de générer tous les arbres possible de taille n
    la class Rand48 vu au debut de l'ue
    
"""

a = 156079716630527


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
        self.n = None
        self.bit_count = 0

    def bit_suivant(self):
        if self.bit_count > 0:
            res = self.n & 1
            self.n = self.n >> 1
            self.bit_count -= 1
            return res
        else:
            self.n = super(Rand48_, self).mrand()
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


rand48 = Rand48(a)
rand48_ = Rand48_(randint(2 ** 40, 2 ** 48))


class BinaryTree(object):
    def __init__(self, left=False, right=False, father=None):
        self.left = left
        self.right = right
        self.father = father

    def is_feuille(self):
        return not self.left and not self.right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_father(self, f):
        self.father = f

    def __repr__(self):
        if self.is_feuille():
            return "eps"
        return "( " + str(self.left) + " " + str(self.right) + " )"


def remy_uniform_random(n, perm=None):
    """
    Génère un arbre de Rémy où les choix de fils sont pré-déterminés

    :param n: taille de l'arbre qu'on souhait générer
    :param perm: liste de permutation pour les arbre de taille n
    :return: un arbe de Remy de taille n
    """

    if n == 0:
        return BinaryTree(father=False)
    k = 1

    left = BinaryTree(father=False)
    right = BinaryTree(father=False)
    root = BinaryTree(father=False, left=left, right=right)

    left.set_father(root)
    right.set_father(root)

    idNodeTree = [root, left, right]

    while k < n:
        id_rand = perm[2 * (k - 1)] if perm else rand48_.gen_n(2 * k)
        F = idNodeTree[id_rand]
        pleft = perm[2 * (k - 1) + 1] if perm else rand48_.bit_suivant()

        E = BinaryTree(father=F.father)
        if F.father:
            if F == F.father.right:
                F.father.set_right(E)
            elif F == F.father.left:
                F.father.set_left(E)

        F.set_father(E)
        leaf = BinaryTree(father=E)

        if pleft == 0:
            E.set_left(F)
            E.set_right(leaf)
        else:
            E.set_right(F)
            E.set_left(leaf)

        idNodeTree.append(E)
        idNodeTree.append(leaf)
        k = k + 1

    # On veux retourner la racine de l'arbre
    node = idNodeTree[0]
    while node.father:
        node = node.father

    return node


def gen_perms(n, i):
    if i >= n:
        return [[]]
    perms = gen_perms(n, i + 1)
    res = []
    for i in range(i * 2 + 1):
        for perm in perms:
            tmp1 = perm.copy()
            tmp2 = perm.copy()
            tmp1 = [i, 0] + tmp1
            tmp2 = [i, 1] + tmp2
            res.append(tmp1)
            res.append(tmp2)
    return res


def gen_perm(n):
    """
    génération de toutes les permutations possible de taille n
    :param n: taille n
    :return: liste de liste de toutes les permutation possible
    """
    return gen_perms(n, 1)


def treeToStr(A):
    if A.left == False and A.right == False:
        return ""
    return "(" + treeToStr(A.left) + ")" + treeToStr(A.right)


def create_all_tree_remy2(n):
    dict_result = defaultdict(lambda: 0)
    for i in gen_perm(n):
        dict_result[treeToStr(remy_uniform_random(n, i))] += 1
    return dict_result


def gnerate_all_tree(n):
    for i in range(n):
        print("Taille ", i, " : ", create_all_tree_remy2(i).items())


# gnerate_all_tree(3)
