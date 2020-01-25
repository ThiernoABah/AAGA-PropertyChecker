import random
import ternary_trie as T3


def construct_ternary(filename, nbMots):
    with open("../Shakespeare/" + filename) as f:
        content = f.readlines()
    candidat = set()
    while len(candidat) < nbMots:
        candidat.add(content[random.randint(0, len(content))][:-1])
    tree = T3.cons(candidat.pop())
    for m in candidat:
        tree = T3.insert(tree, m)
    return tree


def construct_ternary_union(filename, nbMots):
    with open("../Shakespeare/" + filename) as f:
        content = f.readlines()
    candidat = set()
    while len(candidat) < nbMots:
        candidat.add(content[random.randint(0, len(content))][:-1])

    tree = T3.cons(candidat.pop())
    for m in candidat:
        tree = T3.fusion(tree, T3.cons(m))
    return tree


def nbWord(treeA):
    g = 0
    if treeA.val == 0:
        g = 1
        if len(treeA.fils) == 0:
            return 1

    for f in treeA.fils:
        g += nbWord(f)
    return g


def same(treeA, treeB):
    g = True
    if treeA.val != treeB.val and treeA.cle != treeB.cle:
        return False;
    if len(treeA.fils) != len(treeB.fils):
        return False;
    for a, b in zip(treeA.fils, treeB.fils):
        g = g and same(a, b)
    return g

def findBugUnion(filename, filename2, nbMots):
    with open("../Shakespeare/" + filename) as f:
        content = f.readlines()
    with open("../Shakespeare/" + filename2) as f:
        content2 = f.readlines()
    candidat = set()
    candidat2 = set()
    candidat3 = set()
    i = 0
    while len(candidat) < nbMots:
        candidat.add(content[i][:-1])
        candidat3.add(content[i][:-1])
        i = i + 1

    i = 0
    while len(candidat2) < nbMots:
        candidat2.add(content2[i][:-1])
        candidat3.add(content2[i][:-1])
        i = i + 1

    first = candidat.pop()
    first2 = candidat2.pop()
    first3 = candidat3.pop()

    treeInsert = T3.cons(first)
    treeInsert2 = T3.cons(first2)
    treeInsert3 = T3.cons(first3)

    for m in candidat:
        treeInsert = T3.insert(treeInsert, m)
    for m in candidat2:
        treeInsert2 = T3.insert(treeInsert2, m)
    for m in candidat3:
        treeInsert3 = T3.insert(treeInsert3, m)

    treeUnion = T3.fusion(treeInsert, treeInsert2)

    nbMotsUnion = nbWord(treeUnion)
    nbMotsInsert = nbWord(treeInsert3)

    print(treeInsert3.affiche())
    print(treeUnion.affiche())

    print(nbMotsInsert)
    print(nbMotsUnion)

    if (nbMotsUnion != nbMotsInsert):
        print("not same tree : nbWord(treeUnion) != nbWord(treeInsert) ")

findBugUnion("much_ado.txt", "coriolanus.txt", 6)
