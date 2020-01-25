from random import *


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


def remy_uniform_random(n):
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
        id_rand = randint(0, len(idNodeTree) - 1)
        F = idNodeTree[id_rand]

        pleft = randint(0, 1)

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

    #On veux retourner la racine de l'arbre
    node = idNodeTree[0]
    while node.father:
        node = node.father

    return node


def remy_uniform_complete(n, choixNoeud, pileFace):
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
        id_rand = choixNoeud[k - 1]
        F = idNodeTree[id_rand]

        pleft = pileFace[k - 1]

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
    node = idNodeTree[0]
    while node.father:
        node = node.father

    return node


def print_tree(A):
    if A.left == False and A.right == False:
        return "eps"
    return "(" + print_tree(A.left) + ")" + print_tree(A.right)
