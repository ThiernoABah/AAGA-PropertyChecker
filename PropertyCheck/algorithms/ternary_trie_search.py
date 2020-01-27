import random
from ternary_trie import cons, insert, fusion

"""
Construit itérativement et renvoie l'arbre ternaire contenant nbWords mots 
tirés aléatoirement dans les oeuvres de Shakespeare 
"""
def construct_ternary_file(filename, nbWords):
    with open("../Shakespeare/" + filename) as f:
        content = f.readlines()
    words = set()

    while len(words) < nbWords:
        words.add(content[random.randint(0, len(content))][:-1])

    tree = cons(words.pop())

    for m in words:
        tree = insert(tree, m)

    return tree

"""
Construit par fusion et renvoie l'arbre ternaire contenant nbWords mots tirés
 aléatoirement dans les oeuvres de Shakespeare 
"""
def construct_ternary_union(filename, nbMots):
    with open("../Shakespeare/" + filename) as f:
        content = f.readlines()
    candidat = set()
    while len(candidat) < nbMots:
        candidat.add(content[random.randint(0, len(content))][:-1])

    tree = cons(candidat.pop())
    for m in candidat:
        tree = fusion(tree, cons(m))
    return tree

"""
Compare treeA et treeB et vérifie s'ils contiennent les mêmes mots
"""
def same(treeA, treeB):
    g = True
    if treeA.val != treeB.val and treeA.cle != treeB.cle:
        return False
    if len(treeA.fils) != len(treeB.fils):
        return False
    for a, b in zip(treeA.fils, treeB.fils):
        g = g and same(a, b)
    return g


