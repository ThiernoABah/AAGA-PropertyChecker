NB = 0

class Arbre:
    def __init__(self, cle, val, F):
        global NB
        self.id = NB
        NB += 1
        self.cle = cle
        self.val = val
        self.fils = F

    def affiche(self):
        if self.cle == '':
            return ' . '
        g = '( ' + self.cle + (', ' + str(self.val) if self.val != None else '') + '  '
        for f in self.fils:
            g += f.affiche() + ' '
        g += ')'
        return g

    def nbWord(self):
        g = 0
        if self.val == 0:
            g = 1
            if len(self.fils) == 0:
                return 1

        for f in self.fils:
            g += f.nbWord()
        return g

    def get_words(self, prefx):
        words = set()

        if self.cle == '':
            return words
        if self.val == 0:
            words.add(prefx + self.cle)

        words = words.union(self.fils[0].get_words(prefx))
        words = words.union(self.fils[1].get_words(prefx + self.cle))
        words = words.union(self.fils[2].get_words(prefx))

        return words
def cons(mot):
    if mot == '':
        return gener_feuille()
    else:
        if len(mot) == 1:
            return gener_noeud(mot[0], 0, [gener_feuille(), gener_feuille(), gener_feuille()])
        else:
            return gener_noeud(mot[0], None, [gener_feuille(), cons(mot[1:]), gener_feuille()])


def insert(A, mot):
    if mot == '':
        return A
    if A.cle == '':
        return cons(mot)
    if A.cle > mot[0]:
        return gener_noeud(A.cle, A.val, [insert(A.fils[0], mot), A.fils[1], A.fils[2]])
    elif A.cle == mot[0]:
        val = A.val
        if len(mot) == 1:
            val = 0
        return gener_noeud(A.cle, val, [A.fils[0], insert(A.fils[1], mot[1:]), A.fils[2]])
    else:
        val = A.val
        return gener_noeud(A.cle, val, [A.fils[0], A.fils[1], insert(A.fils[2], mot)])


def search(self, mot):
    if mot == '':
        return False
    elif len(self.fils) == 0:
        return False
    elif mot[0] < self.cle:
        return self.fils[0].search(mot)
    elif mot[0] > self.cle:
        return self.fils[2].search(mot)
    elif len(mot) == 1:
        return True if mot[0] == self.cle and self.val == 0 else False
    return self.fils[1].search(mot[1:])


def gener_feuille():
    return Arbre('', None, [])


def gener_noeud(cle, val, F):
    return Arbre(cle, val, F)


def fusion(A, B):
    if A.cle == '':
        return B
    if B.cle == '':
        return A

    if A.cle < B.cle:
        return gener_noeud(A.cle, A.val, [A.fils[0], A.fils[1], fusion(A.fils[2], B)])
    if A.cle > B.cle:
        return gener_noeud(A.cle, A.val, [fusion(A.fils[0], B), A.fils[1], A.fils[2]])

    if A.val != None:
        val = A.val
    else:
        val = B.val
    return gener_noeud(A.cle, val,
                       [fusion(A.fils[0], B.fils[0]), fusion(A.fils[1], B.fils[1]), fusion(A.fils[2], B.fils[2])])