import random
from ternary_trie import cons, insert, fusion


def construct_ternary_file(filename, nbWords):
    """
    Construit itérativement et renvoie l'arbre ternaire contenant nbWords mots
    tirés aléatoirement dans les oeuvres de Shakespeare
    :param filename: un fichier de données
    :param nbWords: nombre de mots à utiliser
    :return: un arbre contenant les mots sélectionner dans le fichier
    """

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
et 
"""


def construct_ternary_union(filename, nbMots):
    """
    Construit par fusion
    :param filename:
    :param nbMots: nombre de mots à rajouter
    :return: renvoie l'arbre ternaire contenant nbWords mots tirés
                aléatoirement dans les oeuvres de Shakespeare
    """
    with open("../Shakespeare/" + filename) as f:
        content = f.readlines()
    candidat = set()
    while len(candidat) < nbMots:
        candidat.add(content[random.randint(0, len(content))][:-1])

    tree = cons(candidat.pop())
    for m in candidat:
        tree = fusion(tree, cons(m))
    return tree


def same(treeA, treeB):
    """
    Compare deux arbre tairnaire et vérifie s'ils contiennent les mêmes mots

    :param treeA: arbre ternaire
    :param treeB: arbre ternaire
    :return: true si treeA = treeB, false dans le cas contraire
    """
    g = True
    if treeA.val != treeB.val and treeA.cle != treeB.cle:
        return False
    if len(treeA.fils) != len(treeB.fils):
        return False
    for a, b in zip(treeA.fils, treeB.fils):
        g = g and same(a, b)
    return g
