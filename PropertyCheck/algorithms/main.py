from RemyProjet import ArbreRemy
from TernarySearchTree.algorithms.RemyV2 import print_tree
from remy_tree_v2 import remy_uniform_complete

"""
Renvoie tous les tirages possibles pour l'algorithme de Rémy pour une liste 
de n éléments
"""
def all_choice_remy2(n):
    res = list()
    choices = list()
    choicesSeen = dict()

    for i in range(n - 1):
        choices.append(0)

    while str(choices) not in choicesSeen:
        res.append(choices.copy())
        choicesSeen[str(choices)] = 1
        for j in range(n):
            if j < n - 1:
                if choices[j] < j + 2:
                    choices[j] += 1
                    break
                else:
                    choices[j] = 0
            else:
                choices[j - 1] += 2 * (n - 1)
    print(res)
    return res


print("...................; gen_perm .................;; ")
all_choice_remy2(3)
print("...................; gen_perm .................;; ")


def get_bin(x, n=0):
    return format(x, 'b').zfill(n)

"""
Génère tous les résultats possibles de pile ou face pour n tirages
"""
def all_pileface(n):
    res = list()
    N = 2 ** (n - 1)
    for i in range(N):
        rpz = [int(char) for char in get_bin(i, (n - 1))]
        res.append(rpz)
    return res

"""
Crée tous les arbres de Rémy de façon déterministe
"""
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


remy = ArbreRemy(0)
remy1 = ArbreRemy(10)
remy2 = ArbreRemy(10)

remy.growingTree(0)
# remy1.growingTree2(10, [0, 2, 1, 4, 3, 5, 0, 1, 7])
# remy2.growingTree2(10, [0, 2, 1, 4, 3, 5, 0, 1, 7])
size = 2
remyV2 = create_all_tree_remy2(size)
print()
print("here all tree of size ", size, "generate for all possible inputs using the first algorithm")
# remy2 = ArbreRemy(2)
# remy2.growingTree2(2, [0, 1])
# print()
print()
print("here all tree of size ", size, "generate for all possible inputs using our algorithm")
